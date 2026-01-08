from flask import *
from app import database
from app.module.library import Library

libraryBP = Blueprint("libraryBP", __name__)

@libraryBP.route("/libraries", methods=["POST"])
def createLibrary():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    library = Library(name=name)
    database.session.add(library)
    database.session.commit()
    return jsonify({"id": library.id, "name": library.name}), 201

@libraryBP.route("/libraries", methods=["GET"])
def listLibraries():
    libraries = Library.query.all()
    result = [{"id": lib.id, "name": lib.name} for lib in libraries]
    return jsonify(result), 200

@libraryBP.route("/libraries/<int:libraryId>", methods=["PUT"])
def updateLibrary(libraryId):
    library = Library.query.get_or_404(libraryId)
    data = request.get_json()
    name = data.get("name")
    if name:
        library.name = name
        database.session.commit()
    return jsonify({"id": library.id, "name": library.name})

@libraryBP.route("/libraries/<int:libraryId>", methods=["DELETE"])
def deleteLibrary(libraryId):
    library = Library.query.get_or_404(libraryId)
    database.session.delete(library)
    database.session.commit()
    return jsonify({"message": "Library deleted"})
