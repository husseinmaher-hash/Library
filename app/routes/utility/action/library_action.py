from flask import jsonify
from sqlalchemy.exc import IntegrityError
from app import database
from app.module.library import Library

def createLibraryAction(data):
    name = data.get("name")
    try:
        library = Library(name=name)
        database.session.add(library)
        database.session.commit()
        return jsonify({"id": library.id, "name": library.name}), 201
    except ValueError as e:
        database.session.rollback()
        return jsonify({"error": str(e)}), 400
    except IntegrityError:
        database.session.rollback()
        return jsonify({"error": "Library already exists"}), 400
    except Exception:
        database.session.rollback()
        return jsonify({"unknown error": "Internal server error"}), 500

def listLibrariesAction():
    libraries = Library.query.all()
    result = [{"id": lib.id, "name": lib.name} for lib in libraries]
    return jsonify(result), 200

def updateLibraryAction(libraryId, data):
    library = Library.query.get_or_404(libraryId)
    name = data.get("name")
    try:
        if name:
            library.name = name
            database.session.commit()
        return jsonify({"id": library.id, "name": library.name}), 200
    except ValueError as e:
        database.session.rollback()
        return jsonify({"error": str(e)}), 400
    except Exception:
        database.session.rollback()
        return jsonify({"error": "Update failed"}), 500

def deleteLibraryAction(libraryId):
    library = Library.query.get_or_404(libraryId)
    try:
        database.session.delete(library)
        database.session.commit()
        return jsonify({"message": "Library deleted"}), 200
    except Exception:
        database.session.rollback()
        return jsonify({"error": "Delete failed"}), 500