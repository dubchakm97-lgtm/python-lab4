from __future__ import annotations

from typing import Iterator

from Books import Tale, Book, OnTheInternetBook


class BookCollection:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Tale | Book | OnTheInternetBook) -> None:
        self.books.append(book)

    def remove_book(self, book: Tale | Book | OnTheInternetBook) -> None:
        self.books.remove(book)

    def __getitem__(self, item: slice | int) -> Tale | Book | OnTheInternetBook | BookCollection:
        if isinstance(item, slice):
            new_lst = BookCollection()
            new_lst.books = self.books[item]
            return new_lst
        return self.books[item]

    def __len__(self) -> int:
        return len(self.books)

    def __iter__(self) -> Iterator[Tale | Book | OnTheInternetBook]:
        return iter(self.books)
