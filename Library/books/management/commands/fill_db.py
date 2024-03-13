from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from books.models import Book, CopyBook, Author, BookIssuanceAccounting, Reader


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self):
        self.a = get_object_or_404(Author,name=self.kwargs["author"])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

