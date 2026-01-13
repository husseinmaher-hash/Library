from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from app import database
from app.module.user import User
from app.module.library import Library

def createUserAction(data):

    try:
        name = data.get("name")
        libraryId = data.get("libraryId")
        library = Library.query.get(libraryId)

        if not library:
            return jsonify({"error": "Library not found"}), 404

        user = User(name=name,libraryId=libraryId)
        database.session.add(user)
        database.session.commit()
        
        return jsonify({
            "id": user.id,
            "name": user.name,
            "libraryId": user.libraryId
        }), 201

    except ValueError as e:
        database.session.rollback()
        return jsonify({"error": str(e)}), 400
    except IntegrityError:
        database.session.rollback()
        return jsonify({"error": "Database integrity violation"}), 400
    except Exception as e:
        database.session.rollback()
        return jsonify({"error": "Internal server error" + str(e)}), 500


def listUserAction():
    user = User.query.all()
    result = [{
        "id": u.id,
        "name": u.name,
        "libraryId": u.libraryId
    } for u in user]
    return jsonify(result), 200


def updateUserAction(userId, data):
    try:
        user = User.query.get(userId)
        name = data.get("name")
        libraryId = data.get("libraryId")

        if name:
            user.name = name
        if libraryId:
            library = Library.query.get(libraryId)
            if not library:
                return jsonify({"error": "Library not found"}), 404
            user.libraryId = libraryId
        
        database.session.commit()
        return jsonify({
            "id": user.id,
            "name": user.name,
            "libraryId": user.libraryId
        }), 200

    except ValueError as e:
        database.session.rollback()
        return jsonify({"error": str(e)}), 400
    
    except Exception:
        database.session.rollback()
        return jsonify({"error": "Update failed"}), 500


def deleteUserAction(userId):
    try:
        user = User.query.get(userId)
        database.session.delete(user)
        database.session.commit()
        return jsonify({"message": "user deleted"}), 200
    except Exception:
        database.session.rollback()
        return jsonify({"error": "Delete failed not found the id"}), 500