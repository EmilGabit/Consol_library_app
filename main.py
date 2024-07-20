"""Основной модуль данного приложения, запуск программы начнется именно с этого модуля."""
from library import Library
from lexicon import LEXICON

# Main function to manage the library
def main():
    """Функция запускает приложение, выводит интерфейс для пользователя."""

    library = Library()

    while True:

        for menu in LEXICON["menu"]:
            print(menu)

        choice: str = input('Введите свой выбор: ')

        if choice == '1':
            title: str = input('Введите название книги: ')
            author: str = input('Введите автора: ')
            try:
                year: int = int(input('Введите год издания: '))
            except ValueError:
                print(LEXICON["value_error"])
            else:
                library.add_book(title, author, year)
        elif choice == '2':
            try:
                book_id: int = int(input('Введите id книги которую хотите удалить: '))
            except ValueError:
                print(LEXICON["value_error"])
            else:
                library.remove_book(book_id)
        elif choice == '3':
            keyword: str = input('Введите название книги или автора: ')
            library.search_book(keyword)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            try:
                book_id: int = int(input('Введите id книги: '))
            except ValueError:
                print(LEXICON["value_error"])
            else:
                print('Выберите статус: 1 - В наличии, 2 - Выдана')
                choice_status: str = input()
                if choice_status == '1':
                    library.changing_status_book(book_id, 'В наличи')
                elif choice_status == '2':
                    library.changing_status_book(book_id, 'Выдана')
                else:
                    print('Не верный выбор, попробуйте ещё раз')
        elif choice == '6':
            break
        else:
            print('Не верный выбор, попробуйте ещё раз')

    print('Выход...')


if __name__ == '__main__':
    main()