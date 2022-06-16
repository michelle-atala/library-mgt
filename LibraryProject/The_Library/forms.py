from django import forms

from .models import book

class Book_search(forms.Form):
    publication_date = forms.DateField(required=False)
    author = forms.CharField(required=False)
    subject_area = forms.CharField(max_length=50)
    title = forms.CharField(required=False)
    shelf_number = forms.CharField(required=False)

