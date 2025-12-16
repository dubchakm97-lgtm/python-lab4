class Tale:
    def __init__(self, title: str, genre: str, isbn: int) -> None:
        self.title = title
        self.genre = genre
        self.isbn = isbn


class Book(Tale):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: int, publishing_house: str) -> None:
        super().__init__(title, genre, isbn)
        self.author = author
        self.year = year
        self.publishing_house = publishing_house


class OnTheInternetBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: int, publishing_house: str,
                 rating: int, popularity: str) -> None:
        super().__init__(title, author, year, genre, isbn, publishing_house)
        self.rating = rating
        self.popularity = popularity
