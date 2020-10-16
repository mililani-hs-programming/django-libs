from django.shortcuts import render

# Create your views here.
#from catalog.models import Book, Author, BookInstance, Genre
from .models import Data

def index(request):
    '''

    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    '''
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def books(request):
    #naming conv: var below should be nameofdatabase_var
    data_var = Data.objects.all()
    for i in data_var:
       print(i.Input)
    return render(request, 'books.html', {'input': data_var})

def authors(request):
    data_var = Data.objects.all()
    for i in data_var:
        print(i.Output)
    return render(request, 'authors.html', {'output': data_var})


