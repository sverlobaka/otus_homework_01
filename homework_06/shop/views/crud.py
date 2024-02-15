from models import db, Book


def get_books_list() -> list[Book]:
    return Book.query.all()

def get_book_by_id(book_id: int) -> Book:
    return Book.query.get_or_404(book_id, f"book #{book_id} not found")

def create_book(name: str) -> Book:
    book = Book(
        name=name,
    )
    db.session.add(book)
    db.session.commit()
    return book

def delete_book(book: Book) -> None:
    db.session.delete(book)
    db.session.commit()

