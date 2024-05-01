from django import forms


class FormLogin(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    
class FormRegister(forms.Form):
    username = forms.CharField(max_length=30, required=True, help_text='Máximo de 30 caracteres')
    email = forms.EmailField(max_length=254, required=True, help_text='Informe um endereço de email válido')
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text='A senha não deve ser muito comum')