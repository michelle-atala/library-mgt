import datetime

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .models import book, borrowed_book
from .forms import Book_search


# Create your views here.
def search(request, *args, **kwargs):  # function called on first access to search.html

    if request.method == 'GET':
        my_form = Book_search()
        my_ctxt = {
            "form": my_form
        }
        return render(request, "search.html", my_ctxt)
    else:  # Render a 400 code

        return HttpResponseBadRequest("<h1>{{request.method}} is not appropriate for this.")


#  DON'T REMOVE THIS INDEX FUNCTION
# def index(request, ctxt=None, *args, **kwargs):
#      my_ctxt = None
#      if ctxt is not None:                          #Checking whether any criteria were passed from forms.
#          title = ctxt.object.title
#          objs = book.objects.filter(title=title)
#          my_ctxt = {
#          "objects": objs
#      }
#      else:
#         objs = list(book.objects.all())
#         my_ctxt = {
#            "objects": objs
#         }
#
#      return render(request, "index.html", my_ctxt)

def index(request):
    my_books = book.objects.all()

    context = {
        'books': my_books

    }

    return render(request, 'index.html', context)


def search_result(request):  # Display search results using index.html # Called after submit button is clicked
    if request.method == 'GET':  # Checking if the request is GET to bind the user data to a fresh form.
        form = Book_search(request.GET)

        if form.is_valid():
            subject_area = form.cleaned_data['subject_area']
            print(subject_area)
            obj = list(book.objects.filter(
                subject_area__icontains=subject_area))  # Using contains to take care of word-spacing.

            my_ctxt = {

                "books": obj,
            }
            # d_title = obj.title
            # my_query = book.objects.filter(title=title)
            print(obj)

            # context = {
            #     "books": my_query
            # }
            return render(request, 'index.html', my_ctxt)



    else:  # Render a 400 code

        return HttpResponseBadRequest("<h1>{{request.method}} is not appropriate for this.")


def borrow(request, id):
    book_id = id
    returned = False
    student = request.user.get_full_name()
    borrow_date = datetime.date.today()
    book_name = book.objects.filter(id=id).title

    transaction = borrowed_book.objects.create(returned=returned, student=student, book_name=book_name, borrow_date=borrow_date,
                                               book_id=book_id)
    transaction.save()
    return render(request, "borrowed.hml")

def report(request):
    obj = borrowed_book.objects.all()
    for x in obj:
        return_date = x.borrow_date + datetime.timedelta(weeks=2)
        time_elapse = datetime.date.today() - return_date
        if time_elapse.days > 10:
            x.penalty_due = 15000
        elif time_elapse.days > 3:
            x.penalty_due = 5000

    obj = borrowed_book.objects.all()

    my_ctxt = {
        "books": obj
    }

    return render(request, "report.html", my_ctxt)

def terms(request, id):
    obj = book.objects.filter(id=id)
    my_ctxt = {
        "book": obj
    }
    return render(request, "terms.html", my_ctxt)



