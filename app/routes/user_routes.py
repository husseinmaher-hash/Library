from flask import Blueprint, request
from .utility.action.user_action import *

libraryBP = Blueprint("userBP", __name__)

@libraryBP.route("/users", methods=["POST"])
def createUser():
    return createUserAction(request.get_json())

@libraryBP.route("/users", methods=["GET"])
def listUser():
    return listUserAction()

@libraryBP.route("/users/<int:usersId>", methods=["PUT"])
def updateUser(usersId):
    return updateUserAction(usersId, request.get_json())

@libraryBP.route("/users/<int:usersId>", methods=["DELETE"])
def deleteUser(usersId):
    return deleteUserAction(usersId)