from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField(label='email')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
class LoginForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    
class RankingForm(forms.Form):
    pregunta_rel = forms.IntegerField(label='pregunta_rel')
    result = forms.IntegerField(label='result')
    pregunta = forms.CharField(label="correcta", max_length=200)
    correcta = forms.CharField(label="correcta", max_length=200)
    incorrecta = forms.CharField(label="incorrecta", max_length=200)