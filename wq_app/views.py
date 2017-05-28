import hashlib
import random
import datetime
from time import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.utils.crypto import get_random_string
from django.urls import reverse

from wq_app import forms
from wq_app.models import UserMeta
from wq_app.logger.logger import get_logger


def generate_activation_key(username):
    secret_key = get_random_string(20)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()


def register(request):
    if request.user.is_authenticated():
        return redirect(home)
    registration_form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            datas = {}
            datas['username'] = form.cleaned_data['username']
            datas['email'] = form.cleaned_data['email']
            datas['first_password_input'] = form.cleaned_data['first_password_input']

            # We generate a random activation key
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            usernamesalt = datas['username']
            if isinstance(usernamesalt, unicode):
                usernamesalt = usernamesalt.encode('utf8')
            datas['activation_key'] = generate_activation_key(usernamesalt)

            datas['email_path'] = "/ActivationEmail.txt"
            datas['email_subject'] = "Activation de votre compte yourdomain"

            form.sendEmail(datas)
            form.save(datas)  # Save the user and his profile

            request.session['registered'] = True  # For display purposes
            return redirect(home)
        else:
            registration_form = form  # Display form with error messages (incorrect fields, etc)
    return render(request, 'siteApp/register.html', locals())


# View called from activation email. Activate user if link didn't expire (48h default), or offer to
# send a second link if the first expired.
def activation(request, key):
    activation_expired = False
    already_active = False
    profile = get_object_or_404(UserMeta, activation_key=key)
    if not profile.user.is_active:
        if timezone.now() > profile.key_expires:
            activation_expired = True  # Display: offer the user to send a new activation link
            id_user = profile.user.id
        else:  # Activation successful
            profile.user.is_active = True
            profile.user.save()

    # If user is already active, simply display error message
    else:
        already_active = True  # Display : error message
    return render(request, 'siteApp/activation.html', locals())


def new_activation_link(request, user_id):
    # todo: check for correct user
    form = forms.RegistrationForm()
    datas = {}
    user = UserMeta.objects.get(id=user_id)
    if user is not None and not user.is_active:
        datas['username'] = user.username
        datas['email'] = user.email
        datas['email_path'] = "/ResendEmail.txt"
        datas['email_subject'] = "Nouveau lien d'activation yourdomain"

        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        usernamesalt = datas['username']
        if isinstance(usernamesalt, unicode):
            usernamesalt = usernamesalt.encode('utf8')
        datas['activation_key'] = hashlib.sha1(salt + usernamesalt).hexdigest()

        user_meta = UserMeta.objects.get(user=user)
        user_meta.activation_key = datas['activation_key']
        user_meta.key_expires = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2),
                                                           "%Y-%m-%d %H:%M:%S")
        user_meta.save()

        form.sendEmail(datas)
        request.session['new_link'] = True  # Display: new link sent

    return redirect(home)


def login_user(request):
    logger = get_logger('views')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        logger.info('logged user in', extra={'username': username})
        return HttpResponseRedirect(reverse('wq_app:index'))
    else:
        # Redisplay the login page with an error message
        render(request, 'wq_app/login_page.html', {'error_message': 'The username or password given are incorrect.'})
