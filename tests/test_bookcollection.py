import pytest
from Books import Tale, Book, OnTheInternetBook
from BookCollection import BookCollection


def test_add_and_len_and_getitem():
    c = BookCollection()
    assert len(c) == 0
    t = Book("T1", "Kanye West", 2025, "Hip_hop", "ISBN-1111", "Roc-a-Fella Records")
    c.add_book(t)
    assert len(c) == 1
    assert c[0] is t


def test_remove():
    c = BookCollection()
    t1 = Tale("T1", "Fantasy", "ISBN-1")
    t2 = Tale("T2", "Drama", "ISBN-2")
    c.add_book(t1)
    c.add_book(t2)
    c.remove_book(t1)
    assert len(c) == 1
    assert c[0] is t2


def test_slice_returns_collection():
    c = BookCollection()
    c.add_book(Tale("A", "G1", "I1"))
    c.add_book(Tale("B", "G2", "I2"))
    c.add_book(Tale("C", "G3", "I3"))
    sub = c[1:3]
    assert isinstance(sub, BookCollection)
    assert len(sub) == 2
    assert sub[0].title == "B"
    assert sub[1].title == "C"


def test_iter():
    c = BookCollection()
    c.add_book(Tale("A", "G", "I1"))
    c.add_book(Tale("B", "G", "I2"))
    titles = [b.title for b in c]
    assert titles == ["A", "B"]

def test_remove_empty():
    c = BookCollection()
    t1 = OnTheInternetBook("T1", "Kanye West", 2025, "Hip_hop", "ISBN-1111", "Roc-a-Fella Records", 10, "HIGH")
    c.add_book(t1)
    c.remove_book(t1)
    with pytest.raises(ValueError):
        c.remove_book(t1)