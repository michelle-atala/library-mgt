from django import forms

from .models import book

class Book_search(forms.Form):
    publication_date = forms.DateField()
    author = forms.CharField(max_length=50)
    subject_area = forms.CharField(max_length=50)
    title = forms.CharField(max_length=50)
    shelf_number = forms.CharField(max_length=10)

