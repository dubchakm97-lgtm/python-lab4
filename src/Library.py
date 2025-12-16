from __future__ import annotations
from BookCollection import BookCollection
from Books import Tale, Book, OnTheInternetBook
from IndexDict import IndexDict


class Library:
    def __init__(self) -> None:
        self.items = BookCollection()
        self.index = IndexDict()

    def add_item(self, element: Tale | Book | OnTheInternetBook, step: int) -> None:
        self.index.add(element, step)
        self.items.add_book(element)

    def del_item(self, element: Tale | Book | OnTheInternetBook, step: int) -> None:
        true_el = self.index.isbn[element.isbn]
        self.index.remove(true_el, step)
        self.items.remove_book(true_el)

    def show_items(self, criterion: str | int, step: int) -> list[str] | str:
        if criterion not in self.index.isbn and criterion not in self.index.author and criterion not in self.index.year:
            raise ValueError(f"[STEP {step}] SHOW criterion='{criterion}' -> NOT_FOUND")
        if criterion in self.index.isbn:
            return self.index.isbn[criterion].title
        elif criterion in self.index.author:
            return [b.title for b in self.index.author[criterion]]
        else:
            return [b.title for b in self.index.year[criterion]]

    def __len__(self) -> int:
        return self.items.__len__()

    def criterion_len(self, criterion: str | int):
        if criterion not in self.index.isbn and criterion not in self.index.author and criterion not in self.index.year:
            raise ValueError('Нет книг с таким параметром')
        if criterion in self.index.isbn:
            return 1
        elif criterion in self.index.author:
            return len(self.index.author[criterion])
        else:
            return len(self.index.year[criterion])

    def __contains__(self, item: Tale | Book | OnTheInternetBook | str | int) -> bool:
        if isinstance(item, (Tale, Book, OnTheInternetBook)):
            return item in self.items.books
        else:
            return item in self.index.year or item in self.index.author or item in self.index.isbn
