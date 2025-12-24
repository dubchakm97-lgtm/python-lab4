class Tale:
    """
    Класс рассказов, буклетов, народных сказаний – любого чтива, которое не имеет автора и год написания
    """
    def __init__(self, title: str, genre: str, isbn: str) -> None:
        """
        Инициализация объектов класса – название рассказа, жанр и международный уникальный код ISBN
        :param title: название рассказа/произведения
        :param genre: жанр произведения
        :param isbn: уникальный международный номер
        """
        self.title = title
        self.genre = genre
        self.isbn = isbn


class Book(Tale):
    """
    Класс книг, которые также имеют автора, год написания произведения и издательство
    """
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, publishing_house: str) -> None:
        """
        Инициализация объектов класса – название произведения, жанр, международный уникальный код ISBN, автор произведения,
        год написания произведения и издательство
        :param title: название произведения
        :param author: автор произведения
        :param year: год написания произведения
        :param genre: жанр произведения
        :param isbn: уникальный международный номер
        :param publishing_house: издательство
        """
        super().__init__(title, genre, isbn)
        self.author = author
        self.year = year
        self.publishing_house = publishing_house


class OnTheInternetBook(Book):
    """
    Класс книг, которые можно найти на популярных интернет-площадках и в электронных библиотеках
    """
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, publishing_house: str,
                 rating: int, popularity: str) -> None:
        """
        Инициализация объектов класса – название произведения, жанр, международный уникальный код ISBN, автор произведения,
        год написания произведения, издательство, средний рейтинг на интернет-платформах и уровень популярности у читателей
        :param title: название произведения
        :param author: автор произведения
        :param year: год написания произведения
        :param genre: жанр произведения
        :param isbn: уникальный международный номер
        :param publishing_house: издательство
        :param rating: рейтинг произведения на электронных платформах
        :param popularity: уровень популярности у читателей
        """
        super().__init__(title, author, year, genre, isbn, publishing_house)
        self.rating = rating
        self.popularity = popularity
