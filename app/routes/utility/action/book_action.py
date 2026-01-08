from flask import *
from app import database
from app.module.books import Book
from app.module.library import Library



def createBookAction(data):
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





def listBooksAction(books):
    result = [{
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "libraryId": book.libraryId
    } for book in books]
    return jsonify(result), 200



def updateBookAction(bookId):
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


def deleteBookAction(bookId):
    book = Book.query.get_or_404(bookId)
    database.session.delete(book)
    database.session.commit()
    return jsonify({"message": "Book deleted"})
