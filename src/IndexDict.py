from __future__ import annotations

from Books import Tale, Book, OnTheInternetBook

from typing import Iterator


class IndexDict:
    def __init__(self) -> None:
        self.isbn = {}
        self.author = {}
        self.year = {}

    def add(self, book: Tale | Book | OnTheInternetBook, step: int) -> None:
        if type(book) is not Tale:
            if book.isbn in self.isbn:
                raise ValueError(f"[STEP {step}] ADD_BOOK isbn={book.isbn} -> ERROR duplicate_isbn")
            self.isbn[book.isbn] = book
            if book.author not in self.author:
                self.author[book.author] = [book]
            else:
                self.author[book.author].append(book)
            if book.year not in self.year:
                self.year[book.year] = [book]
            else:
                self.year[book.year].append(book)
        else:
            if book.isbn in self.isbn:
                raise ValueError(f"[STEP {step}] ADD_TALE isbn={book.isbn} -> ERROR duplicate_isbn")
            self.isbn[book.isbn] = book

    def remove(self, book: Tale | Book | OnTheInternetBook, step: int) -> None:
        if book.isbn not in self.isbn:
            raise ValueError(f"[STEP {step}] REMOVE isbn={book.isbn} -> ERROR not_found")
        item = self.isbn[book.isbn]
        if type(item) is not Tale:
            del self.isbn[item.isbn]
            self.author[item.author].remove(item)
            if len(self.author[item.author]) == 0:
                del self.author[item.author]
            self.year[item.year].remove(item)
            if len(self.year[item.year]) == 0:
                del self.year[item.year]
        else:
            del self.isbn[item.isbn]

    def __getitem__(self, item: str | int) -> Tale | Book | OnTheInternetBook | list[Tale | Book | OnTheInternetBook]:
        if item in self.isbn:
            return self.isbn[item]
        elif item in self.author:
            return self.author[item]
        elif item in self.year:
            return self.year[item]
        else:
            raise KeyError(item)

    def __len__(self) -> int:
        return len(self.isbn)

    def __iter__(self) -> Iterator[str]:
        return iter(self.isbn)
