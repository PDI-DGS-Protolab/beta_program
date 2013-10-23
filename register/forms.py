from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    desc  = forms.CharField(max_length=100, required=True)
    url   = forms.URLField(max_length=250, required=False)