from django.db import models
class book(models.Model):
    publication_date= models.DateField()
    author = models.TextField(max_length=50)
    subject_area = models.CharField(max_length=50)
    title = models.TextField(max_length=50)
    shelf_number = models.CharField(max_length=10)


#class borrowed(models.Model):
# username
    # book_borrowed
  # date_borrowed
   #date_returned
   #penalty
class Student(models.Model):
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    student_number=models.CharField(max_length=12)
