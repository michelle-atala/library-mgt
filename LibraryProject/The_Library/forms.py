from django import forms

from .models import book

class Book_search(forms.Form):
    class Meta:
        model=book
        fields=[
        'publication_date',
        'author',
        'subject_area',
        'title',
        'shelf_number',

        ]
