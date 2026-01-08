from flask import Blueprint, request
from .utility.action.library_action import *

libraryBP = Blueprint("libraryBP", __name__)

@libraryBP.route("/libraries", methods=["POST"])
def createLibrary():
    return createLibraryAction(request.get_json())

@libraryBP.route("/libraries", methods=["GET"])
def listLibraries():
    return listLibrariesAction()

@libraryBP.route("/libraries/<int:libraryId>", methods=["PUT"])
def updateLibrary(libraryId):
    return updateLibraryAction(libraryId, request.get_json())

@libraryBP.route("/libraries/<int:libraryId>", methods=["DELETE"])
def deleteLibrary(libraryId):
    return deleteLibraryAction(libraryId)