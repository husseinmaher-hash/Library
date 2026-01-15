from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from app import database
from app.module.books import Book
from app.module.library import Library

def createBookAction(data):

    try:
        title = data.get("title")
        author = data.get("author")
        libraryId = data.get("libraryId")

        library = Library.query.get(libraryId)
        if not library:
            return jsonify({"error": "Library not found"}), 404

        book = Book(title=title, author=author, libraryId=libraryId)
        database.session.add(book)
        database.session.commit()
        
        return jsonify({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "libraryId": book.libraryId
        }), 201

    except ValueError as e:
        database.session.rollback()
        return jsonify({"error": str(e)}), 400
    
    except IntegrityError:
        database.session.rollback()
        return jsonify({"error": "Database integrity violation"}), 400
    
    except Exception:
        database.session.rollback()
        return jsonify({"error": "Internal server error"}), 500


def listBooksAction():
    books = Book.query.all()
    result = [{
        "id": b.id,
        "title": b.title,
        "author": b.author,
        "libraryId": b.libraryId
    } for b in books]
    return jsonify(result), 200

def updateBookAction(bookId, data):
    try:
        book = Book.query.get(bookId)
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
            book.libraryId = libraryId
        
        database.session.commit()
        return jsonify({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "libraryId": book.libraryId
        }), 200

    except ValueError as e:
        database.session.rollback()
        return jsonify({"error": str(e)}), 400
    
    except Exception:
        database.session.rollback()
        return jsonify({"error": "Update failed"}), 500


def transferLibrariesBooksAction(bookId,data):
    try:
        book = Book.query.get(bookId)
        title = data.get("title")
        author = data.get("author")
        libraryId = data.get("libraryId")

        if title:
            return jsonify({"error:": "cant change the titles"}), 400
        if author:
            return jsonify({"error:": "cant change the author"}), 400
        if libraryId:
            library = Library.query.get(libraryId)
            if not library:
                return jsonify({"error": "Library not found"}), 404
            
            elif library == libraryId:
                return jsonify({"error": "this books in this library"}), 404
            
            book.libraryId = libraryId
        
        database.session.commit()
        return jsonify({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "libraryId": book.libraryId
        }), 200

    except ValueError as e:
        database.session.rollback()
        return jsonify({"error": str(e)}), 400
    except Exception:
        database.session.rollback()
        return jsonify({"error": "Update failed"}), 500




def deleteBookAction(bookId):
    try:
        book = Book.query.get(bookId)
        database.session.delete(book)
        database.session.commit()
        return jsonify({"message": "Book deleted"}), 200
    except Exception:
        database.session.rollback()
        return jsonify({"error": "Delete failed not found the id"}), 500