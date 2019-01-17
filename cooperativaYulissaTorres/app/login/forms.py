from django import forms

class FormularioLogin(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'type':'text', 'name':'log', 'id':'user_login', 'class':'input', 'placeholder':'Username', 'value':'', 'size':'20'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'type':'password', 'name':'pwd', 'id':'user_pass', 'class':'input', 'placeholder':'Password', 'value':'', 'size':'20'})) 