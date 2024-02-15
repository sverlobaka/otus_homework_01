from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import BadRequest, NotFound

from models import Book
from . import crud

books_app = Blueprint(
    "books_app",
    __name__,
    url_prefix="/books"
)


@books_app.get("/", endpoint="list")
def get_books_list():
    return render_template(
        "books_list.html",
        books=crud.get_books_list(),
    )


@books_app.get("/<int:book_id>/", endpoint="details")
def get_book_by_id_or_raise(book_id: int):
    book: Book = crud.get_book_by_id(book_id)

    return render_template(
        "details.html",
        book=book,
    )


@books_app.route("/create/", endpoint="create", methods=["GET", "POST"])
def create_new_book():
    if request.method == "GET":
        return render_template("create.html")

    book_name = request.form.get("book_name", "")
    book_name = book_name.strip()
    if not book_name:
        raise BadRequest("`book_name` field required")

    book = crud.create_book(name=book_name)
    flash(f"Created book {book.name}", category="success")
    url = url_for("books_app.details", book_id=book.id)
    return redirect(url)


@books_app.route(
    "/<int:book_id>/confirm-delete/",
    endpoint="delete",
    methods=["GET", "POST"],
)
def delete_book(book_id: int):
    book = crud.get_book_by_id(book_id)
    if request.method == "GET":
        return render_template(
            "confirm-delete.html",
            book=book
        )
    flash(f"Deleted book {book.name}", category="danger")
    crud.delete_book(book)
    url = url_for("books_app.list")
    return redirect(url)


@books_app.get("/history", endpoint="history")
def history_shop():
    return render_template("history.html")