from django.contrib import admin
from .models import book

@admin.register(book)
class bookAdmin(admin.ModelAdmin):
    list_display = ("title","author","shelf_number")
# Register your models here.
