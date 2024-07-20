from services import load_library, save_library
from lexicon import LEXICON

class Library:
    """Класс Библиотека
    Данный класс при инициализации создает атребут books типа список путем вызова функции  load_library
    Класс обладает следующими методами:
    - add_book - добавление книги в библиотеку
    - display_books - отображение всех книг в библиотеке
    - remove_book - удаление книги по id
    - search_book - поиск книги по названию или автору
    - changing_status_book - Изменения статуса книги
    """

    def __init__(self):
        """Метод создает атрибут класса"""
        self.books: list = load_library()  # список книг


    def display_books(self):
        """Метод принимает экземпляр класса и возвращает данные из библиотеки"""
        if len(self.books):
            for book in self.books:
                print(f"\n| ID: {book['id']} | Книга: {book['title']} | Автор: {book['author']} | Год: {book['year']} "
                    f"| Статус: {book['status']} |\n")
        else:
            print("\n*В библиотеке нет книг*")

    def add_book(self, title: str, author: str, year: int):
        """Метод принимает аргументы и добавляет данные в библиотеку:
        - title - Название книги
        - author - Автор книги
        - year - Год издания книги
        """
        book = {
            'id': len(self.books) + 1,
            'title': title,
            'author': author,
            'year': year,
            'status': 'В наличии'
        }
        self.books.append(book)
        save_library(self.books)
        print(f'\n*Книга {title} успешно добавлена*')


    def remove_book(self, book_id: int):
        """Метод удаляет книгу из библиотеки
        Метод принимает аргумент book_id - ID книги в библиотеке
        после чего удалят объект из списка и сохраняет обновленный
        спиок в библиотеке """
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                save_library(self.books)
                print(f"\n*Книга '{book['title']}' успешно удалена*")
                return None
        else:
            print(f'{LEXICON["not_book"]}{book_id}')


    def search_book(self, keyword: str):
        """Метод осуществляет поиск книги в библиотеке.
        Метод принимает аргумент "keyword" - название или автор книги"""
        count = 0
        for book in self.books:
            if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower():
                count += 1
                print(f"{'_' * 95}\n"
                      f"| ID: {book['id']}, | Title: {book['title']}, | Author: {book['author']}, | Year: {book['year']}, "
                      f"| Status: {book['status']} |\n"
                      f"{'_' * 95}")
        if not count:
            print(f'{LEXICON["not_book"]}{keyword}')


    def changing_status_book(self, book_id: int, status: str):
        """Метод меняет статус книги в библиотеке.
        Метод принимает аргументы book_id - ID книги
        в библиотеке, status - статус книги,
        и обновляет данные в библиотеке."""
        for book in self.books:
            if book_id == book['id']:
                book['status'] = status
                save_library(self.books)
                print(f'\n*Статус книги успешно изменен*')
                return None
        else:
            print(f'{LEXICON["not_book"]}{book_id}')





