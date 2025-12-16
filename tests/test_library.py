import pytest
from Books import Tale, Book, OnTheInternetBook
from Library import Library


def make_tale(isbn="ISBN-T1"):
    return Tale("Tale", "Fantasy", isbn)


def make_book(isbn="ISBN-B1", author="A", year=2000, title="Book"):
    return Book(title=title, author=author, year=year, genre="G", isbn=isbn, publishing_house="P")


def make_ebook(isbn="ISBN-B1", author="A", year=2000, title="Book"):
    return OnTheInternetBook(title=title, author=author, year=year, genre="G", isbn=isbn, publishing_house="P",
                             rating=5, popularity="HIGH")


def test_add_item_updates_collection_and_index():
    lib = Library()
    b = make_ebook(isbn="ISBN-1", author="Orwell", year=1949, title="1984")
    lib.add_item(b, step=1)
    assert len(lib) == 1
    assert lib.index.isbn["ISBN-1"] is b
    assert lib.index.author["Orwell"] == [b]
    assert lib.index.year[1949] == [b]


def test_show_items_isbn_returns_title():
    lib = Library()
    b = make_book(isbn="ISBN-1", title="1984")
    lib.add_item(b, step=1)
    assert lib.show_items("ISBN-1", step=2) == "1984"


def test_delete_removes_from_indexes():
    lib = Library()
    b = make_book("ISBN-1", "Orwell", 1949, "1984")
    lib.add_item(b, step=1)
    lib.del_item(b, step=2)
    assert "ISBN-1" not in lib.index.isbn
    assert "Orwell" not in lib.index.author
    assert 1949 not in lib.index.year
    assert len(lib) == 0


def test_search_by_author_returns_titles():
    lib = Library()
    lib.add_item(make_book("ISBN-1", "Orwell", 1949, "1984"), step=1)
    lib.add_item(make_book("ISBN-2", "Orwell", 1945, "Animal Farm"), step=2)
    assert lib.show_items("Orwell", step=3) == ["1984", "Animal Farm"]


def test_library_rejects_duplicate_isbn():
    lib = Library()
    b1 = make_book("ISBN-1", "Orwell", 1949, "1984")
    b2 = make_book("ISBN-1", "Orwell", 1945, "Animal Farm")
    lib.add_item(b1, step=1)
    with pytest.raises(ValueError):
        lib.add_item(b2, step=2)
