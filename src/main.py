from __future__ import annotations
import random
from Library import Library
from Books import Tale, Book, OnTheInternetBook
from IndexDict import IndexDict

words = ["Sky", "Code", "Story", "Night", "Dream", "Rocket", "Python", "Library", "Shadow", "Ocean"]
genres = ["Fantasy", "Sci-Fi", "Drama", "Detective", "Poetry", "Non-fiction", "Horror", "Hip-Hop"]
first_names = ["Ivan", "Anna", "Mark", "Elena", "Oleg", "Max", "Kanye", "Pavel"]
last_names = ["Orlov", "Smirnov", "Volkov", "West", "Petrov", "Ivanov", "Kuznetsova"]
pubs = ["LitRes", "AST", "Eksmo", "O'Reilly", "Penguin", "HarperCollins"]
popularity_levels = ["low", "medium", "high"]


def is_valid_text(s: str) -> bool:
    """
    Проверяет валидность строки, чтобы в строке название, а не цифры
    :param s: строка
    :return: True or False
    """
    s = s.strip()
    if not s:
        return False
    return all(ch.isalpha() or ch in " -'" for ch in s)


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """
    Функция, запускающая симуляцию библиотеки и действий в ней
    :param steps: кол-во действий, выполняемых в библиотеке
    :param seed: начальное число, из которого начинается генерация псевдослучайных чисел
    :return: None
    """
    lib = Library()
    if seed is not None:
        random.seed(seed)
    acts = ['add new tale', 'add new book', 'add new popular book', 'remove book', 'searching book by author',
            'searching book by genre',
            'searching book by isbn', 'update of index', 'get unexisted book']

    # Всевозможные действия, исполняемые в библиотеке

    for step in range(1, steps + 1):
        act = random.choice(acts)  # Определяем случайным образом, что будем делать
        try:
            if act == 'add new tale':  # Добавляем новый рассказ в библиотеку
                while True:
                    DESIRE = input(
                        "Хотите ли Вы добавить в библиотеку случайную книгу: (да/нет) ")  # Проверяем, хочет ли пользователь добавить случайную книгу в библиотеку
                    if DESIRE == "да":
                        title = f"{random.choice(words)} {random.choice(words)}"
                        genre = random.choice(genres)
                        isbn_num = str(random.randint(1000, 9999))
                        isbn = f"ISBN-{step:04d}-{isbn_num}"
                        break
                    elif DESIRE == "нет":
                        title = input("Введите название рассказа: ")
                        genre = input("Введите жанр произведения: ")
                        isbn_num = input("Введите числовое значение ISBN: ")
                        isbn = f"ISBN-{step:04d}-{isbn_num}"
                        break
                    else:
                        print('Введите да или нет.')
                if (
                        not is_valid_text(title)
                        or not is_valid_text(genre)
                        or not isbn_num.isdigit()
                ):
                    raise ValueError('Неверные названия полей объекта')
                tale = Tale(
                    title=title,
                    genre=genre,
                    isbn=isbn
                )
                lib.add_item(tale, step)
                print(f"[STEP {step}] ADD_TALE isbn={tale.isbn} title='{tale.title}' genre='{tale.genre}' -> OK")
            elif act == 'add new book':  # Добавляем новую книгу в библиотеку
                while True:
                    DESIRE = input(
                        "Хотите ли Вы добавить в библиотеку случайную книгу: (да/нет) ")  # Проверяем, хочет ли пользователь добавить случайную книгу в библиотеку
                    if DESIRE == "да":
                        title = f"{random.choice(words)} {random.choice(words)}"
                        genre = random.choice(genres)
                        isbn_num = str(random.randint(1000, 9999))
                        isbn = f"ISBN-{step:04d}-{isbn_num}"
                        author = f"{random.choice(first_names)} {random.choice(last_names)}"
                        year = random.randint(1950, 2025)
                        publishing_house = random.choice(pubs)
                        break
                    elif DESIRE == "нет":
                        title = input("Введите название книги: ")
                        genre = input("Введите жанр произведения: ")
                        isbn_num = input("Введите числовое значение ISBN: ")
                        isbn = f"ISBN-{step:04d}-{isbn_num}"
                        author = input("Введите автора произведения: ")
                        year = input("Введите год создания произведения: ")
                        publishing_house = input("Введите название издательства: ")
                        break
                    else:
                        print('Введите да или нет.')
                if (
                        not is_valid_text(title)
                        or not is_valid_text(genre)
                        or not isbn_num.isdigit()
                        or not is_valid_text(author)
                        or not is_valid_text(publishing_house)
                ):
                    raise ValueError('Неверные названия полей объекта')
                book = Book(
                    title=title,
                    genre=genre,
                    isbn=isbn,
                    author=author,
                    year=int(year),
                    publishing_house=publishing_house,
                )
                lib.add_item(book, step)
                print(
                    f"[STEP {step}] ADD_BOOK isbn={book.isbn} title='{book.title}' author='{book.author}' year={book.year} genre='{book.genre}' pub='{book.publishing_house}' -> OK")
            elif act == 'add new popular book':  # Добавляем новую книгу, которая есть на интернет-платформах, в библиотеку
                while True:
                    DESIRE = input(
                        "Хотите ли Вы добавить в библиотеку случайную книгу: (да/нет) ")  # Проверяем, хочет ли пользователь добавить случайную книгу в библиотеку
                    if DESIRE == "да":
                        title = f"{random.choice(words)} {random.choice(words)}"
                        genre = random.choice(genres)
                        isbn_num = str(random.randint(1000, 9999))
                        isbn = f"ISBN-{step:04d}-{isbn_num}"
                        author = f"{random.choice(first_names)} {random.choice(last_names)}"
                        year = random.randint(1950, 2025)
                        publishing_house = random.choice(pubs)
                        rating = random.randint(1, 5)
                        popularity = random.choice(popularity_levels)
                        break
                    elif DESIRE == "нет":
                        title = input("Введите название книги: ")
                        genre = input("Введите жанр произведения: ")
                        isbn_num = input("Введите числовое значение ISBN: ")
                        isbn = f"ISBN-{step:04d}-{isbn_num}"
                        author = input("Введите автора произведения: ")
                        year = input("Введите год создания произведения: ")
                        publishing_house = input("Введите название издательства: ")
                        rating = input("Введите средний рейтинг книги на интернет-платформах: ")
                        popularity = input("Введите уровень популярности произведения среди читателей")
                        break
                    else:
                        print('Введите да или нет.')
                if (
                        not is_valid_text(title)
                        or not is_valid_text(genre)
                        or not isbn_num.isdigit()
                        or not is_valid_text(author)
                        or not is_valid_text(publishing_house)
                        or not is_valid_text(popularity)
                ):
                    raise ValueError('Неверные названия полей объекта')
                ob = OnTheInternetBook(
                    title=title,
                    genre=genre,
                    isbn=isbn,
                    author=author,
                    year=int(year),
                    publishing_house=publishing_house,
                    rating=int(rating),
                    popularity=popularity
                )
                lib.add_item(ob, step)
                print(
                    f"[STEP {step}] ADD_ONLINE isbn={ob.isbn} title='{ob.title}' author='{ob.author}' year={ob.year} rating={ob.rating} popularity='{ob.popularity}' -> OK")
            elif act == 'remove book':  # Удаляем книгу из библиотеки
                if len(lib) == 0:
                    print(f"[STEP {step}] REMOVE -> SKIP library_empty")
                else:
                    item = random.randrange(len(lib.items))
                    book = lib.items[item]
                    lib.del_item(book, step)
                    print(f"[STEP {step}] REMOVE isbn={book.isbn} title='{book.title}' -> OK")
            elif act == 'searching book by author':  # Ищем книгу в библиотеке по автору
                author = f"{random.choice(first_names)} {random.choice(last_names)}"
                print(
                    f"[STEP {step}] FIND_AUTHOR author='{author}' -> {len(lib.show_items(author, step))} items, titles={lib.show_items(author, step)}")
            elif act == 'searching book by genre':  # Ищем книгу в библиотеке по жанру
                genre = random.choice(genres)
                titles = [b.title for b in lib.items if b.genre == genre]
                print(
                    f"[STEP {step}] FIND_GENRE genre='{genre}' -> {len(titles)} items, titles={titles}")
            elif act == 'searching book by isbn':  # Ищем книгу в библиотеке по уникальному номеру
                if len(lib) == 0 or random.random() < 0.5:
                    isbn = f"ISBN-{random.randint(1, 9999):04d}-{random.randint(1000, 9999)}"
                else:
                    isbn = lib.items[random.randrange(len(lib.items))].isbn
                print(
                    f"[STEP {step}] FIND_ISBN isbn='{isbn}' -> 1 items, titles={lib.show_items(isbn, step)}")
            elif act == 'update of index':  # Обновляем индексы книг (автор, год, номер) в словарях
                new_index = IndexDict()
                for book in lib.items:
                    new_index.add(book, step)
                lib.index = new_index
                print(f"[STEP {step}] REINDEX -> OK count={len(lib.index)}")
            else:  # Ищем несуществующую книгу в библиотеке
                fake_isbn = '4:44'
                lib.show_items(fake_isbn, step)
        except ValueError as e:
            print(f'{e}')
        except Exception as e1:
            print(f"Возникла ошибка! {e1}")


def main():
    """
    Основная функция программы, запускающая псевдосимуляцию библиотеки
    :return: None
    """
    while True:
        try:  # Вводим количество шагов-действий, исполняемых в библиотеке
            steps = int(input('Введите количество шагов симуляции: '))
            break
        except ValueError:
            print("ERROR: wrong amount of steps")
    while True:
        try:  # Вводим параметр seed
            seed = int(input('Введите seed: '))
            if seed == -1:
                seed = None
            break
        except ValueError:
            print("ERROR: wrong seed")
    run_simulation(steps, seed)  # Запускаем псевдосимуляцию


if __name__ == "__main__":
    main()
