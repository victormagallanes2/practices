from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class ChangePasswordForm(forms.Form):

    password = forms.CharField(
        label='New password',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password_two = forms.CharField(
        label='Repeat password',
        min_length=5,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password_two(self):
        """Comprueba que password y password_two sean iguales."""
        password = self.cleaned_data['password']
        password_two = self.cleaned_data['password_two']
        if password != password_two:
            raise forms.ValidationError('The passwords do not match.')
        return password_two