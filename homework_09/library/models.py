from django.db import models


class Genre(models.Model):
    class Meta:
        verbose_name_plural = "Genres"

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=64)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name="books",
    )

    def __str__(self):
        return f"{self.name} ({self.genre.name})"

