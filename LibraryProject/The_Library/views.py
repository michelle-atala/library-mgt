from django.shortcuts import render,redirect
from django.template import loader

from django.http import HttpResponse
from .forms import SignUp_form
from .models import Student

def login (request):
    template=loader.get_template("login.html")

    return HttpResponse(template.render())

def sign_up (request):
    if request.method=='POST':
        form=SignUp_form(request.POST)

        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            user_name=form.cleaned_data['user_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            print(form.cleaned_data)

            object =Student.objects.create(first_name=first_name,last_name=last_name,user_name=user_name,email=email,password=password)
            object.save()
            return redirect(login)


    else:
        form1=SignUp_form()

        context={
            "form":form1

        }
        return render(request,'sign_up.html',context)













    #template=loader.get_template("sign_up.html")
        #HttpResponse(template.render())


# Create your views here.

