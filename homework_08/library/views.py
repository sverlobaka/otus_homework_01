from django.http import HttpRequest
from django.shortcuts import render
from .models import Genre, Book


def index_view(request):
    books = (
        Book
        .objects.select_related("genre")
        .all()
    )
    context = {
        "books": books,
    }
    return render(
        request,
        "library/book-list.html",
        context
    )


def genres_with_books(request: HttpRequest):
    context = {
        "genres": (
            Genre
            .objects
            .prefetch_related("books")
            .all()
        )
    }
    return render(
        request,
        "library/genres-with-books.html",
        context,
    )