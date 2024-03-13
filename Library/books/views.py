from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import BookForm, ReaderForm, BookIssuanceAccountingForm
from .models import Book, CopyBook, Genre, Author, Reader, BookIssuanceAccounting


class BookListView(ListView):
    queryset = Book.objects.order_by("name")
    template_name = "books/book-list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    form_class = BookForm
    template_name = "books/book-detail.html"
    context_object_name = "book"


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book-form.html"
    success_url = reverse_lazy("books:list")


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book-form.html"
    success_url = reverse_lazy("books:list")


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("books:list")


class CopyBookListView(LoginRequiredMixin, ListView):
    model = CopyBook
    fields = "__all__"
    context_object_name = "copies_books"
    template_name = "books/copy-list.html"


class CopyBookCreateView(LoginRequiredMixin, CreateView):
    model = CopyBook
    fields = "__all__"
    template_name = "books/copy-book.html"
    success_url = reverse_lazy('books:copy_last')


def last_copy_book(request: HttpRequest):
    context = {"copy": (CopyBook.objects.all().last())}
    return render(request,"books/copy-last.html", context)


class CopyDetailView(LoginRequiredMixin, DetailView):
    model = CopyBook
    template_name = "books/copy-detail.html"

class CopyDeleteView(LoginRequiredMixin, DeleteView):
    model = CopyBook
    success_url = reverse_lazy("books:copy_list")


class GenreListView(ListView):
    model = Genre
    template_name = "books/genre-list.html"
    context_object_name = "genres"

class GenreCreateView(LoginRequiredMixin, CreateView):
    model = Genre
    fields = "__all__"
    template_name = "books/genre-form.html"
    success_url = reverse_lazy("books:genre_list")


class GenreDeleteView(LoginRequiredMixin, DeleteView):
    model = Genre
    success_url = reverse_lazy("books:genre_list")


class AuthorListView(ListView):
    queryset = Author.objects.order_by("name")
    template_name = "books/author-list.html"
    context_object_name = "authors"


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = "__all__"
    template_name = "books/author-form.html"
    success_url = reverse_lazy("books:author_list")


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    fields = "__all__"
    template_name = "books/author-form.html"
    success_url = reverse_lazy("books:author_list")


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy("books:author_list")


class ReaderListView(LoginRequiredMixin, ListView):
    queryset = Reader.objects.order_by("name")
    template_name = "books/reader-list.html"
    context_object_name = "readers"



class ReaderCreateView(LoginRequiredMixin, CreateView):
    model = Reader
    form_class = ReaderForm
    template_name = "books/reader-form.html"
    success_url = reverse_lazy("books:reader_list")


class ReaderDetailView(LoginRequiredMixin, DetailView):
    model = Reader
    form_class = ReaderForm
    template_name = "books/reader-detail.html"
    context_object_name = "reader"


class ReaderUpdateView(LoginRequiredMixin, UpdateView):
    model = Reader
    form_class = ReaderForm
    template_name = "books/reader-form.html"
    success_url = reverse_lazy("books:reader_list")


class ReaderDeleteView(LoginRequiredMixin, DeleteView):
    model = Reader
    success_url = reverse_lazy("books:reader_list")


class BookIssuanceAccountingListView(LoginRequiredMixin, ListView):
    model = BookIssuanceAccounting
    template_name = "books/accounting-books-list.html"
    context_object_name = "books"



class BookIssuanceAccountingDetailView(LoginRequiredMixin, DetailView):
    model = BookIssuanceAccounting
    form_class = BookIssuanceAccountingForm
    template_name = "books/accounting-book-detail.html"
    context_object_name = "book"


class BookIssuanceAccountingCreateView(LoginRequiredMixin, CreateView):
    model = BookIssuanceAccounting
    form_class = BookIssuanceAccountingForm
    template_name = "books/accounting-book-form.html"
    success_url = reverse_lazy("books:accounting_books_list")


class BookIssuanceAccountingUpdateView(LoginRequiredMixin, UpdateView):
    model = BookIssuanceAccounting
    form_class = BookIssuanceAccountingForm
    template_name = "books/accounting-book-form.html"
    success_url = reverse_lazy("books:accounting_books_list")


def debt_list(request):
    context = {"debt": (BookIssuanceAccounting.objects.filter(return_book=False))}
    return render(request,"books/debt-list.html", context)
