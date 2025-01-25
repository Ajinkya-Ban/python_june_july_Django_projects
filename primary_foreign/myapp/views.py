from django.shortcuts import render
from .models import Book, Author
# Create your views here.

def authors(request):
    authors = Author.objects.prefetch_related('books').all()
    return render(request,"myapp/authors.html",{"authors":authors})
