from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password',max_length=100)