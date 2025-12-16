import pytest
from Books import Tale, Book, OnTheInternetBook
from IndexDict import IndexDict


def make_tale(isbn="ISBN-T1"):
    return Tale("Tale", "Fantasy", isbn)


def make_book(isbn="ISBN-B1", author="A", year=2000, title="Book"):
    return Book(title=title, author=author, year=year, genre="G", isbn=isbn, publishing_house="P")

def make_ebook(isbn="ISBN-B1", author="A", year=2000, title="Book"):
    return OnTheInternetBook(title=title, author=author, year=year, genre="G", isbn=isbn, publishing_house="P", rating=5, popularity="HIGH")


def test_add_tale_indexes_only_isbn():
    idx = IndexDict()
    t = make_tale("ISBN-T1")
    idx.add(t, step=1)
    assert idx.isbn["ISBN-T1"] is t
    assert idx.author == {}
    assert idx.year == {}


def test_add_book_indexes_isbn_author_year():
    idx = IndexDict()
    b = make_ebook(isbn="ISBN-1", author="Orwell", year=1949, title="1984")
    idx.add(b, step=1)
    assert idx.isbn["ISBN-1"] is b
    assert idx.author["Orwell"] == [b]
    assert idx.year[1949] == [b]


def test_add_same_isbn_raises():
    idx = IndexDict()
    b1 = make_book(isbn="ISBN-1", title="T1")
    b2 = make_book(isbn="ISBN-1", title="T2")
    idx.add(b1, step=1)
    with pytest.raises(ValueError):
        idx.add(b2, step=2)


def test_remove_book_cleans_author_year_when_empty():
    idx = IndexDict()
    b = make_book(isbn="ISBN-1", author="A", year=2000)
    idx.add(b, step=1)
    idx.remove(b, step=2)
    assert "ISBN-1" not in idx.isbn
    assert "A" not in idx.author
    assert 2000 not in idx.year


def test_remove_one_of_two_keeps_keys():
    idx = IndexDict()
    b1 = make_book(isbn="ISBN-1", author="A", year=2000, title="T1")
    b2 = make_book(isbn="ISBN-2", author="A", year=2000, title="T2")
    idx.add(b1, step=1)
    idx.add(b2, step=1)
    idx.remove(b1, step=2)
    assert "ISBN-1" not in idx.isbn
    assert idx.author["A"] == [b2]
    assert idx.year[2000] == [b2]


def test_getitem_by_isbn_author_year():
    idx = IndexDict()
    b1 = make_book(isbn="ISBN-1", author="A", year=2000, title="T1")
    b2 = make_book(isbn="ISBN-2", author="A", year=2001, title="T2")
    idx.add(b1, step=1)
    idx.add(b2, step=1)
    assert idx["ISBN-1"] is b1
    assert idx["A"] == [b1, b2]
    assert idx[2001] == [b2]


def test_getitem_missing_raises_keyerror():
    idx = IndexDict()
    with pytest.raises(KeyError):
        _ = idx["NOPE"]