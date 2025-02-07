from django.contrib import admin
from django.urls import path
from .views import BookListCreateView, BookDetailsView

urlpatterns = [

    path('books/',BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>', BookDetailsView.as_view(), name="book-details")
]

# http:localhost:8000/books   ---> 1. display all the list
                              #--> 2. Store the data

# http:localhost:8000/books/1  ---> Searching, updation and deletion