from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
class LoginForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)