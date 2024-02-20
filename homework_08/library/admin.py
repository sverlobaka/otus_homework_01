from django.contrib import admin
from . models import Genre, Book

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = "id", "name", "genre"
    list_display_links = "id", "name"