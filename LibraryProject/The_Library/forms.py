from django import forms
<<<<<<< HEAD
from .models import Student
=======
>>>>>>> ea596d074a4de83edc79ae16798a6c242e75673e

class SignUp_form(forms.Form):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    user_name=forms.CharField(max_length=50)
    email=forms.EmailField()
    password=forms.CharField(max_length=50)

<<<<<<< HEAD
class Login_form(forms.Form):
    user_name=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)

def clean_data (self):
    user_name=self.cleaned_data.get("user_name")
    password=self.cleaned_data.get("password")

    data=Student.objects.filter(user_name=user_name,password=password)
    if not data :
        raise forms.ValidationError("Username or password is incorrect")

    return user_name,password


=======
>>>>>>> ea596d074a4de83edc79ae16798a6c242e75673e
