from flask import Blueprint
from flask import render_template


books_app = Blueprint(
    "books_app",
    __name__,
    url_prefix="/about"
)


@books_app.get("/books/", endpoint="list")
def get_books_list():
    books = ["The Hitchhiker's Guide to the Galaxy", "Good Omens", "Трудно быть богом"]
    return render_template(
        "index.html", books=books)


@books_app.get("/", endpoint="history")
def history_shop():
    return render_template("history.html")
