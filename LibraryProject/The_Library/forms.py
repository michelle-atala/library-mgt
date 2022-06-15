from django import forms

class SignUp_form(forms.Form):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    user_name=forms.CharField(max_length=50)
    email=forms.EmailField()
    password=forms.CharField(max_length=50)

