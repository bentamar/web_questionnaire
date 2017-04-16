from django import forms
from django.core import validators


class RegistrationForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Nom d\'utilisateur', 'class': 'form-control input-perso'}), max_length=30, min_length=3,
                               validators=[isValidUsername, validators.validate_slug])
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control input-perso'}), max_length=100,
                             error_messages={'invalid': ("Email invalide.")}, validators=[isValidEmail])
    password1 = forms.CharField(label="", max_length=50, min_length=6,
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Mot de passe', 'class': 'form-control input-perso'}))
    password2 = forms.CharField(label="", max_length=50, min_length=6,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer mot de passe',
                                                                  'class': 'form-control input-perso'}))

    # recaptcha = ReCaptchaField()

    # Override clean method to check password match
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            self._errors['password2'] = ErrorList([u"Le mot de passe ne correspond pas."])

        return self.cleaned_data

    # Override of save method for saving both User and Profile objects
    def save(self, datas):
        u = User.objects.create_user(datas['username'],
                                     datas['email'],
                                     datas['password1'])
        u.is_active = False
        u.save()
        profile = Profile()
        profile.user = u
        profile.activation_key = datas['activation_key']
        profile.key_expires = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2),
                                                         "%Y-%m-%d %H:%M:%S")
        profile.save()
        return u

    # Sending activation email ------>>>!! Warning : Domain name is hardcoded below !!<<<------
    # The email is written in a text file (it contains templatetags which are populated by the method below)
    def sendEmail(self, datas):
        link = "http://yourdomain.com/activate/" + datas['activation_key']
        c = Context({'activation_link': link, 'username': datas['username']})
        f = open(MEDIA_ROOT + datas['email_path'], 'r')
        t = Template(f.read())
        f.close()
        message = t.render(c)
        # print unicode(message).encode('utf8')
        send_mail(datas['email_subject'], message, 'yourdomain <no-reply@yourdomain.com>', [datas['email']],
                  fail_silently=False)
