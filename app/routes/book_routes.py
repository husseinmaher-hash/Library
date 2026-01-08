from flask import *
from app import database
from app.module.books import Book
from app.module.library import Library

bookBP = Blueprint("bookBP", __name__)

@bookBP.route("/books", methods=["POST"])
def createBook():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    libraryId = data.get("libraryId")
    if not (title and author and libraryId):
        return jsonify({"error": "title, author, and libraryId required"}), 400

    library = Library.query.get(libraryId)
    if not library:
        return jsonify({"error": "Library not found"}), 404

    book = Book(title=title, author=author, library=library)
    database.session.add(book)
    database.session.commit()
    return jsonify({
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "libraryId": book.libraryId
    }), 201

@bookBP.route("/books", methods=["GET"])
def listBooks():
    books = Book.query.all()
    result = [{
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "libraryId": book.libraryId
    } for book in books]
    return jsonify(result), 200

@bookBP.route("/books/<int:bookId>", methods=["PUT"])
def updateBook(bookId):
    book = Book.query.get_or_404(bookId)
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    libraryId = data.get("libraryId")

    if title:
        book.title = title
    if author:
        book.author = author
    if libraryId:
        library = Library.query.get(libraryId)
        if not library:
            return jsonify({"error": "Library not found"}), 404
        book.library = library

    database.session.commit()
    return jsonify({
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "libraryId": book.libraryId
    })

@bookBP.route("/books/<int:bookId>", methods=["DELETE"])
def deleteBook(bookId):
    book = Book.query.get_or_404(bookId)
    database.session.delete(book)
    database.session.commit()
    return jsonify({"message": "Book deleted"})
