from __future__ import annotations

from typing import Iterator

from Books import Tale, Book, OnTheInternetBook


class BookCollection:
    """
    Класс, хранящий список всех книг в библиотеке
    """
    def __init__(self) -> None:
        """
        Инициализация списка всех книг, лежащих в библиотеке
        """
        self.books = []

    def add_book(self, book: Tale | Book | OnTheInternetBook) -> None:
        """
        Добавление книги в библиотеку
        :param book: книга (объект одного из классов Tale, Book, OnTheInternetBook)
        :return: None
        """
        self.books.append(book)

    def remove_book(self, book: Tale | Book | OnTheInternetBook) -> None:
        """
        Удаление одной книги из библиотеки
        :param book: книга (объект одного из классов Tale, Book, OnTheInternetBook)
        :return: None
        """
        self.books.remove(book)

    def __getitem__(self, item: slice | int) -> Tale | Book | OnTheInternetBook | BookCollection:
        if isinstance(item, slice):
            new_lst = BookCollection()
            new_lst.books = self.books[item]
            return new_lst
        return self.books[item]

    def __len__(self) -> int:
        """
        Метод, возвращающий количество книг в списке books
        :return: Количество книг в списке books (во всей библиотеке)
        """
        return len(self.books)

    def __iter__(self) -> Iterator[Tale | Book | OnTheInternetBook]:
        return iter(self.books)
