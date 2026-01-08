from flask import *
from app import database
from app.module.books import Book
from app.module.library import Library
from .utility.action.book_action import * 

bookBP = Blueprint("bookBP", __name__)

@bookBP.route("/books", methods=["POST"])
def createBook():
    data = request.get_json()
    return createBookAction(data)
    

@bookBP.route("/books", methods=["GET"])
def listBooks():
    books = Book.query.all()
    return listBooksAction(books)

@bookBP.route("/books/<int:bookId>", methods=["PUT"])
def updateBook(bookId):
    return updateBookAction(bookId)


@bookBP.route("/books/<int:bookId>", methods=["DELETE"])
def deleteBook(bookId):
    return deleteBookAction(bookId)