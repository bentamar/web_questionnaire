import datetime

from captcha.fields import ReCaptchaField
from django import forms
from django.core import validators
from django.core.mail import send_mail
from django.forms.utils import ErrorList
from django.contrib.auth.models import User

from wq_app.models import UserMeta


class RegistrationForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control'}), max_length=30, min_length=3,
                               validators=[validators.validate_slug])
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}), max_length=100,
                             error_messages={'invalid': 'Email is invalid.'}, validators=[validators.EmailValidator])
    first_password_input = forms.CharField(label='', max_length=50, min_length=6,
                                           widget=forms.PasswordInput(
                                               attrs={'placeholder': 'Password', 'class': 'form-control'}))
    second_password_input = forms.CharField(label='', max_length=50, min_length=6,
                                            widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password',
                                                                              'class': 'form-control'}))

    recaptcha = ReCaptchaField()

    def clean(self):
        first_password_input = self.cleaned_data.get('first_password_input')
        second_password_input = self.cleaned_data.get('second_password_input')

        if first_password_input and first_password_input != second_password_input:
            self._errors['second_password_input'] = ErrorList([u'The passwords do not match.'])

        return self.cleaned_data

    # Override of save method for saving both User and Profile objects
    def save(self, datas):
        u = User.objects.create_user(datas['username'],
                                     datas['email'],
                                     datas['first_password_input'])
        u.is_active = False
        u.save()
        profile = UserMeta()
        profile.user = u
        profile.activation_key = datas['activation_key']
        profile.key_expires = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2),
                                                         '%Y-%m-%d %H:%M:%S')
        profile.save()
        return u

    # Sending activation email ------>>>!! Warning : Domain name is hardcoded below !!<<<------
    # The email is written in a text file (it contains templatetags which are populated by the method below)
    def sendEmail(self, activation_key, username, email):
        link = 'http://yourdomain.com/activate/{activation_key}'.format(activation_key=activation_key)
        c = Context({'activation_link': link, 'username': username})
        f = open(MEDIA_ROOT + datas['email_path'], 'r')
        t = Template(f.read())
        f.close()
        message = t.render(c)
        # print unicode(message).encode('utf8')
        send_mail(datas['email_subject'], message, 'yourdomain <no-reply@yourdomain.com>', [email],
                  fail_silently=False)
