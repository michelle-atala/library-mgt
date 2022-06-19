from django.db import models


class book(models.Model):
    publication_date = models.DateField()
    author = models.TextField(max_length=50)
    subject_area = models.CharField(max_length=50)
    title = models.TextField(max_length=50)
    shelf_number = models.CharField(max_length=10)
    borrowed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title},{self.author},{self.shelf_number}"


class borrowed_book(models.Model):
    returned = models.BooleanField()
    book_id = models.ForeignKey(book, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100, default="")  # Remove default on Fresh DB creation
    student = models.CharField(max_length=100)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True)
    penalty_due = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student},{self.book_id},{self.borrow_date},{self.return_date},{self.returned},{self.penalty_due}"


# class borrowed(models.Model):
# username
# book_borrowed
# date_borrowed
# date_returned
# penalty
# class Student(models.Model):
#     first_name = models.CharField(max_length=50, default=None)
#     last_name = models.CharField(max_length=50, default=None)
#     user_name = models.CharField(max_length=50)
#     password = models.CharField(max_length=20)
#     email = models.EmailField(max_length=250, default=None)
#
#     # student_number=models.CharField(max_length=12)
#
#     def __str__(self):
#         return f"{self.first_name},{self.last_name},{self.user_name},{self.email}"
