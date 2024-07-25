import pytest

@pytest.fixture(autouse=True)
def clean_test_file():
    with open("library.json", "w"):
        pass
