import pytest
from services.services import load_library, save_library
import json

def create_test_data(test_data):
    with open('./library.json', 'w') as file:
        json.dump(test_data, file, indent=4)

def test_load_library_empty():
    create_test_data([])
    assert load_library() == []

def test_load_library():
    test_data = [
        {
            "id": 1,
            "title": "sdfsf",
            "author": "sfsf",
            "year": 5,
            "status": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"
        }
    ]
    create_test_data(test_data)
    assert test_data == load_library()


def test_save_library_empty():
    save_library([])
    result = load_library()
    assert result == []

def test_save_library():
    test_data = [
        {
            "id": 1,
            "title": "sdfsf",
            "author": "sfsf",
            "year": 5,
            "status": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"
        }
    ]

    save_library(test_data)
    result = load_library()
    assert result == test_data
