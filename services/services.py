import json
"""В моделу содержатся вспомогательные функции для работа с JSON
load_library - чтение данных из файла JSON
save_library - сохранение данных в JSON файл"""

def load_library() -> list:
    """Функция не принимает никаких аргументов.
    Функция открывает и считывает файл json, записывает данные в переменную
    в случае если файл не обнаружен, функция создать пустой список
    Возвращаемое значение list. """
    try:
        with open('./library.json', 'r') as file:
            library: list = json.load(file)
    except FileNotFoundError:
        library: list = []
    return library


def save_library(library: list[dict]):
    """Функция принимает список с вложенным словарем
    и записывает данные в json файл. В случае если ранее файла не было,
    файл создается.
    Аргументы функции:
    - library - словарь с вложенным списком."""

    with open('./library.json', 'w') as file:
        json.dump(library, file, indent=4)



