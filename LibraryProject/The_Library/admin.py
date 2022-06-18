from django.contrib import admin
from .models import book,Student
admin.site.register(book)
@admin.register(Student)

class Students(admin.ModelAdmin):
    list_display=("first_name","last_name","user_name","email")

# Register your models here.
