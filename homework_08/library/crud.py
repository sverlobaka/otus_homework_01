from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "library/book-list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "library/book-detail.html"
    context_object_name = "books"
