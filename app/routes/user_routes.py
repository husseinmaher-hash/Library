from flask import Blueprint, request
from .utility.action.user_action import *

userBP = Blueprint("userBP", __name__)

@userBP.route("/users", methods=["POST"])
def createUser():
    return createUserAction(request.get_json())

@userBP.route("/users", methods=["GET"])
def listUser():
    return listUserAction()

@userBP.route("/users/<int:usersId>", methods=["PUT"])
def updateUser(usersId):
    return updateUserAction(usersId, request.get_json())

@userBP.route("/users/<int:usersId>", methods=["DELETE"])
def deleteUser(usersId):
    return deleteUserAction(usersId)




