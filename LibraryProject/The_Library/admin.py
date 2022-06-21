from django.contrib import admin
from .models import book,borrowed_book


@admin.register(book)

class bookAdmin(admin.ModelAdmin):
    list_display = ("title","author","shelf_number")

@admin.register(borrowed_book)

class borrowed_bookAdmin(admin.ModelAdmin):
    list_display = ("student","book_id","borrow_date","return_date","returned","penalty_due")
# Register your models here.
