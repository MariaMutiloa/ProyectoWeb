from django import forms

class LoginForm(forms.Form):
    correo = forms.EmailField(
        label='✉️ Ingresar usuario',
        widget=forms.TextInput(attrs={'class': 'cajaentradatexto'})
    )
    password = forms.CharField(
        label='🔐 Ingresar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'cajaentradatexto'})
    )



