from django.db import models


class book(models.Model):
    publication_date= models.DateField()
    author = models.TextField(max_length=50)
    subject_area = models.CharField(max_length=50)
    title = models.TextField(max_length=50)
    shelf_number = models.CharField(max_length=10)
    borrowed= models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title},{self.author},{self.shelf_number}"

class borrowed_book(models.Model):
    returned= models.BooleanField()
    book_id=models.ForeignKey(book,on_delete=models.CASCADE)
    student=models.CharField(max_length=100)
    borrow_date=models.DateField()
    return_date=models.DateField()
    penalty_due=models.IntegerField()

    def __str__(self):
        return f"{self.student},{self.book_id},{self.borrow_date},{self.return_date},{self.returned},{self.penalty_due}"




#class borrowed(models.Model):
# username
    # book_borrowed
  # date_borrowed
   #date_returned
   #penalty

