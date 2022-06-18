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
    first_name=models.CharField(max_length=50,default='Samson')
    last_name=models.CharField(max_length=50,default='Wanendeya')
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=250,default='someone@gmail.com')
    #student_number=models.CharField(max_length=12)

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.user_name},{self.email}"

