from django.test import TestCase

from library.models import Book, Genre


class GenreTestCase(TestCase):

    def setUp(self):
        print("START OF TEST")
        self.genre = Genre.objects.create(name="фэнтези")

    def tearDown(self):
        print("END OF TEST")

    def test_db(self):
        self.assertEqual(str(self.genre), "фэнтези")

    def test_model_genre_book(self):
        book = Book.objects.create(genre=self.genre, name="Кровь и железо")
        self.assertEqual(str(book), "Кровь и железо (фэнтези)")
