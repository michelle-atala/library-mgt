from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse
def login (request):
    template=loader.get_template("login.html")

    return HttpResponse(template.render())

def sign_up (request):
    template=loader.get_template("sign_up.html")

    return HttpResponse(template.render())

# Create your views here.

