from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    booklist = Book.objects.all()

    context= {
        'booklist': booklist
    }

    return render(request, 'index.html', context)
