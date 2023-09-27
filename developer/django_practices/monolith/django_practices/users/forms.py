from django import forms
from django.contrib.auth.models import User


class SingupForm(forms.Form):

    username     = forms.CharField(label="Usuario",widget=forms.TextInput())
    first_name   = forms.CharField(label="Nombre",required=False,widget=forms.TextInput())
    last_name    = forms.CharField(label="Apellido",required=False,widget=forms.TextInput())
    email        = forms.EmailField(label="Correo",required=False,widget=forms.TextInput())
    is_active    = forms.CharField(label="Activo",required=False,widget=forms.TextInput())
    password     = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=True))
    password_two = forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=True))


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            p = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de usuario ya existe')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            p = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email ya registrado')

    def clean_password_two(self):
        password = self.cleaned_data['password']
        password_two = self.cleaned_data['password_two']
        if password == password_two:
            pass
        else:
            raise forms.ValidationError('Password no coinciden')
