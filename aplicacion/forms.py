from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label = 'Email del usuario')
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirmar Contraseña', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required = True)