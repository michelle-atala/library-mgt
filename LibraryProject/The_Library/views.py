from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .models import book
from .forms import Book_search


# Create your views here.
def search(request, *args, **kwargs):
    # Michelle please uncomment the code when you need to see if the errors disappear after the fields creation.

    if request.method == 'GET':  # Checking if the request is GET to bind the user data to a fresh form.
        form = Book_search(request.GET)

        if form.is_valid():
            title = request.cleaned_data['title']
            obj = list(book.objects.filter(title__icontains=title))  # Using contains to take care of word-spacing.

            my_ctxt = {
                "object": obj
            }
            return redirect(search_result(request, my_ctxt))



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


def search_result(request, ctxt):  # Display search results using index.html
    title = ctxt.title
    my_query = book.objects.filter(title=title)

    context = {
        "books": my_query
    }
    return render(request, 'index.html', context)
