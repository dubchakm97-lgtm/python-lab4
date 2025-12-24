from __future__ import annotations
from BookCollection import BookCollection
from Books import Tale, Book, OnTheInternetBook
from IndexDict import IndexDict


class Library:
    """
    Класс библиотеки книг
    """
    def __init__(self) -> None:
        """
        Инициализация двух классов, которые характеризуют список всех книг библиотеки и словари, по которым книги распределяются
        """
        self.items = BookCollection()
        self.index = IndexDict()

    def add_item(self, element: Tale | Book | OnTheInternetBook, step: int) -> None:
        """
        Добавление книги в библиотеку
        :param element: книга (объект одного из классов Tale, Book, OnTheInternetBook)
        :param step: шаг, который характеризует последовательный номер выполнения действия (добавления книги)
        :return: None
        """
        self.index.add(element, step)
        self.items.add_book(element)

    def del_item(self, element: Tale | Book | OnTheInternetBook, step: int) -> None:
        """
        Удаление книги из библиотеки
        :param element: книга (объект одного из классов Tale, Book, OnTheInternetBook)
        :param step: шаг, который характеризует последовательный номер выполнения действия (удаления книги)
        :return: None
        """
        true_el = self.index.isbn[element.isbn]
        self.index.remove(true_el, step)
        self.items.remove_book(true_el)

    def show_items(self, criterion: str | int, step: int) -> list[str] | str:
        """
        Метод, показывающий книги по определенному критерию (книги одного автора, одного года написания или книга по ISBN)
        :param criterion: критерий, определяющий книгу/книги
        :param step: шаг, который характеризует последовательный номер выполнения действия (поиск книг)
        :return: None
        """
        if criterion not in self.index.isbn and criterion not in self.index.author and criterion not in self.index.year:
            raise ValueError(f"[STEP {step}] SHOW criterion='{criterion}' -> NOT_FOUND")
        if criterion in self.index.isbn:
            return self.index.isbn[criterion].title
        elif criterion in self.index.author:
            return [b.title for b in self.index.author[criterion]]
        else:
            return [b.title for b in self.index.year[criterion]]

    def __len__(self) -> int:
        """
        Метод, показывающий количество книг в библиотеке
        :return: кол-во книг в библиотеке
        """
        return self.items.__len__()

    def criterion_len(self, criterion: str | int) -> int:
        """
        Метод, показывающий количество книг в библиотеке по определённому критерию
        :param criterion: критерий, определяющий книгу
        :return: кол-во книг, удовлетворяющих критерию
        """
        if criterion not in self.index.isbn and criterion not in self.index.author and criterion not in self.index.year:
            raise ValueError('Нет книг с таким параметром')
        if criterion in self.index.isbn:
            return 1
        elif criterion in self.index.author:
            return len(self.index.author[criterion])
        else:
            return len(self.index.year[criterion])

    def __contains__(self, item: Tale | Book | OnTheInternetBook | str | int) -> bool:
        """
        Метод, определяющий, есть ли определенная книга/книги в библиотеке
        :param item: книга (объект одного из классов Tale, Book, OnTheInternetBook) или поле одного из этих объектов
        :return: True | False
        """
        if isinstance(item, (Tale, Book, OnTheInternetBook)):
            return item in self.items.books
        else:
            return item in self.index.year or item in self.index.author or item in self.index.isbn
