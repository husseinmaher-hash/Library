
from app.routes.utility.action.book_action import *
from app import database
from run import app

def test_createBookAction_Library_not_found():
    data = {"title": "dump", "author": 'Ali', "libraryId": 0}

    with app.app_context():
        response, status_code = createBookAction(data)

    assert status_code == 404
    assert response.get_json()["error"] == "Library not found"


def test_createUserAction_ValueError():
    data = {"title": "", "libraryId": 1}

    with app.app_context():
        response, status_code = createBookAction(data)

    assert status_code == 400
    assert response.get_json()["error"] == "Book title cannot be empty"



"""
def test_createBookAction_IntegrityError():
    data =     {
        "author": "g" * 103,
        "libraryId": 1,
        "title": "None"
    }

    with app.app_context():
        response, status_code = createBookAction(data)

    assert status_code == 400
    assert response.get_json()["error"] == "Database integrity violation"

"""



def test_createBookAction_Internal_server_error():
    data = {"title": "dump", "author": 2, "libraryId": 1}

    with app.app_context():
        response, status_code = createBookAction(data)

    assert status_code == 500
    assert response.get_json()["error"] == "Internal server error"




def test_updateBookAction_library_not_found():
    bookId  = 1
    data = {"title": "dump", "author": "the dumper", "libraryId": 9999} 

    with app.app_context():
        response, status_code = updateBookAction(bookId, data)

    assert status_code == 404
    assert response.get_json()["error"] == "Library not found"
