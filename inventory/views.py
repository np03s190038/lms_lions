from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import BookForm, BookSearchForm
import csv
from django.db.models import Q

#from .filters import BooksFilter

from .forms import AddBookForm

from .models import Books

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def addbook(request):
    my_form = AddBookForm()
    if request.method == "POST":
        my_form = AddBookForm(request.POST, request.FILES)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Books.objects.create(**my_form.cleaned_data)
            return redirect('dashboard')
        else:
            print(my_form.errors)
    context = {
        "form" : my_form
    }
    return render(request, 'addbook.html', context)

def download(request):
    return render(request, 'download.html')

def issuebook(request):
    return render(request, 'issuebook.html')

def dashboard(request):
    books = Books.objects.all()
    return render(request, 'inventory.html', {'books':books})

def updateBooks(request, pk):
    books = Books.objects.get(id=pk)
    my_form = AddBookForm(instance=books)

    if request.method == "POST":
        my_form = AddBookForm(request.POST, request.FILES, instance=books)
        if my_form.is_valid():
            my_form.save()
            return redirect('dashboard')

    context = {"form": my_form}
    return render(request, 'addbook.html', context)

def deleteBook(request, pk):
    books = Books.objects.get(id=pk)
    if request.method == "POST":
        books.delete()
        return redirect('dashboard')
    context={'item':books}
    return render(request, 'deletemessage.html', context)


def bookDownload(request):
    items = Books.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] =  'attachement: filename="BookList.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['book_Name', 'author_Name', 'author_image', 'genre', 'quantity'])
    for obj in items:
            writer.writerow([obj.book_Name, obj.author_Name, obj.author_Image, obj.genre, obj.quantity])
    return response

def searchBook(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    
    if q:
        items = Books.objects.filter(genre__icontains=q)
        context = {'query':q, 'items': items}
        template = 'inventory.html'
    else:        
        template = 'inventory.html'
        context = {}
    return render(request, template, context)