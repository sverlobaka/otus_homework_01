from django.contrib import admin

from . models import Genre
from . models import Author
from . models import Book
from . models import CopyBook
from . models import Reader
from . models import BookIssuanceAccounting


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = "id", "name", "author", "genre", "description"
    list_display_links = "id", "name"


@admin.register(CopyBook)
class CopyBookAdmin(admin.ModelAdmin):
    list_display = "id", "book", "registration_date"
    list_display_links = "id", "book"


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = "id", "name", "address", "email"
    list_display_links = "id", "name"


@admin.register(BookIssuanceAccounting)
class BookIssuanceAccountingAdmin(admin.ModelAdmin):
    list_display = "id", "reader", "book", "copy_book", "date_of_issue", "return_date", "return_book"
    list_display_links = "id", "reader"
