from django.db import models
from django.db.models import DateTimeField
from django.db.models import PositiveIntegerField


class Genre(models.Model):
    class Meta:
        verbose_name_plural = "Жанры"

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    class Meta:
        verbose_name_plural = "Авторы"

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        verbose_name_plural = "Книги"

    name = models.CharField(max_length=64, unique=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name="books",
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name="books",
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CopyBook(models.Model):
    class Meta:
        verbose_name_plural = "Экземпляры книг"

    registration_date = DateTimeField(
        auto_now_add=True,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.book.name


class Reader(models.Model):
    class Meta:
        verbose_name_plural = "Библиотечная карточка читателя"

    name = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=999)
    email = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class BookIssuanceAccounting(models.Model):
    class Meta:
        verbose_name_plural = "Учет выдачи книг"

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    copy_book = models.OneToOneField(
        CopyBook,
        on_delete=models.CASCADE,
    )
    reader = models.ForeignKey(
        Reader,
        on_delete=models.CASCADE,
        related_name="debt_books",
    )
    date_of_issue = models.DateField(auto_now_add=True)
    return_date = models.DateField(auto_now=False)
    return_book = models.BooleanField(null=True, blank=True)

