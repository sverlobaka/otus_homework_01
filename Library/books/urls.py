"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


app_name = "books"

urlpatterns = [
    path(
        "",
         views.BookListView.as_view(),
         name="list"
    ),
    path(
        "detail/<int:pk>",
        views.BookDetailView.as_view(),
        name="detail"
    ),
    path(
        "create",
        views.BookCreateView.as_view(),
        name="create"
    ),
    path(
        "update/<int:pk>/",
        views.BookUpdateView.as_view(),
        name="update"
    ),
    path(
        "delete/<int:pk>/",
        views.BookDeleteView.as_view(),
        name="delete"
    ),
    path(
        "create_copy/",
        views.CopyBookCreateView.as_view(),
        name="create_copy"
    ),
    path(
        "copy_list/",
        views.CopyBookListView.as_view(),
        name="copy_list"
    ),
    path(
        "copy_last/",
        views.last_copy_book,
        name="copy_last"
    ),
    path(
        "copy_detail/<int:pk>",
        views.CopyDetailView.as_view(),
        name="copy_detail"
    ),
    path(
        "copy_delete/<int:pk>/",
        views.CopyDeleteView.as_view(),
        name="copy_delete"
    ),
    path(
        "create_genre",
        views.GenreCreateView.as_view(),
        name="create_genre"
    ),
    path(
        "genre_list",
        views.GenreListView.as_view(),
        name="genre_list"
    ),
    path(
        "genre_delete/<int:pk>/",
        views.GenreDeleteView.as_view(),
        name="genre_delete"
    ),
    path(
        "author_list",
        views.AuthorListView.as_view(),
        name="author_list"
    ),
    path(
        "create_author",
        views.AuthorCreateView.as_view(),
        name="create_author"
    ),
    path(
        "author_update/<int:pk>",
        views.AuthorUpdateView.as_view(),
        name="author_update"
    ),
    path(
        "author_delete/<int:pk>/",
        views.AuthorDeleteView.as_view(),
        name="author_delete"
    ),
    path(
        "reader_list",
        views.ReaderListView.as_view(),
        name="reader_list"
    ),
    path(
        "reader_create",
        views.ReaderCreateView.as_view(),
        name="reader_create"
    ),
    path(
        "reader_detail/<int:pk>",
        views.ReaderDetailView.as_view(),
        name="reader_detail"
    ),
    path(
        "reader_update/<int:pk>",
        views.ReaderUpdateView.as_view(),
        name="reader_update"
    ),
    path(
        "reader_delete/<int:pk>",
        views.ReaderDeleteView.as_view(),
        name="reader_delete"
    ),
    path(
        "accounting_books_list",
        views.BookIssuanceAccountingListView.as_view(),
        name="accounting_books_list"
    ),
    path(
        "accounting_books_create",
        views.BookIssuanceAccountingCreateView.as_view(),
        name="accounting_books_create"
    ),
    path(
        "accounting_book_detail/<int:pk>",
        views.BookIssuanceAccountingDetailView.as_view(),
        name="accounting_book_detail"
    ),
    path(
        "accounting_book_update/<int:pk>",
        views.BookIssuanceAccountingUpdateView.as_view(),
        name="accounting_book_update"
    ),
    path(
        "accounting_book_update/<int:pk>",
        views.BookIssuanceAccountingUpdateView.as_view(),
        name="accounting_book_update"
    ),
    # path(
    #     "author_by_book",
    #     views.AuthorBookListView.as_view(),
    #     name="author_by_book"
    # ),
    path(
        "debt_list/",
        views.debt_list,
        name="debt_list"
    ),
]

