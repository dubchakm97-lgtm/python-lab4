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


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    lib = Library()
    if seed is not None:
        random.seed(seed)
    acts = ['add new tale', 'add new book', 'add new popular book', 'remove book', 'searching book by author',
            'searching book by genre',
            'searching book by isbn', 'update of index', 'get unexisted book']
    for step in range(1, steps + 1):
        act = random.choice(acts)
        try:
            if act == 'add new tale':
                tale = Tale(
                    title=f"{random.choice(words)} {random.choice(words)}",
                    genre=random.choice(genres),
                    isbn=f"ISBN-{step:04d}-{random.randint(1000, 9999)}"
                )
                lib.add_item(tale, step)
                print(f"[STEP {step}] ADD_TALE isbn={tale.isbn} title='{tale.title}' genre='{tale.genre}' -> OK")
            elif act == 'add new book':
                book = Book(
                    title=f"{random.choice(words)} {random.choice(words)}",
                    genre=random.choice(genres),
                    isbn=f"ISBN-{step:04d}-{random.randint(1000, 9999)}",
                    author=f"{random.choice(first_names)} {random.choice(last_names)}",
                    year=random.randint(1950, 2025),
                    publishing_house=random.choice(pubs),
                )
                lib.add_item(book, step)
                print(
                    f"[STEP {step}] ADD_BOOK isbn={book.isbn} title='{book.title}' author='{book.author}' year={book.year} genre='{book.genre}' pub='{book.publishing_house}' -> OK")
            elif act == 'add new popular book':
                ob = OnTheInternetBook(
                    title=f"{random.choice(words)} {random.choice(words)}",
                    genre=random.choice(genres),
                    isbn=f"ISBN-{step:04d}-{random.randint(1000, 9999)}",
                    author=f"{random.choice(first_names)} {random.choice(last_names)}",
                    year=random.randint(1950, 2025),
                    publishing_house=random.choice(pubs),
                    rating=random.randint(1, 5),
                    popularity=random.choice(popularity_levels)
                )
                lib.add_item(ob, step)
                print(
                    f"[STEP {step}] ADD_ONLINE isbn={ob.isbn} title='{ob.title}' author='{ob.author}' year={ob.year} rating={ob.rating} popularity='{ob.popularity}' -> OK")
            elif act == 'remove book':
                if len(lib) == 0:
                    print(f"[STEP {step}] REMOVE -> SKIP library_empty")
                else:
                    item = random.randrange(len(lib.items))
                    book = lib.items[item]
                    lib.del_item(book, step)
                    print(f"[STEP {step}] REMOVE isbn={book.isbn} title='{book.title}' -> OK")
            elif act == 'searching book by author':
                author = f"{random.choice(first_names)} {random.choice(last_names)}"
                print(
                    f"[STEP {step}] FIND_AUTHOR author='{author}' -> {len(lib.show_items(author, step))} items, titles={lib.show_items(author, step)}")
            elif act == 'searching book by genre':
                genre = random.choice(genres)
                titles = [b.title for b in lib.items if b.genre == genre]
                print(
                    f"[STEP {step}] FIND_GENRE genre='{genre}' -> {len(titles)} items, titles={titles}")
            elif act == 'searching book by isbn':
                if len(lib) == 0 or random.random() < 0.5:
                    isbn = f"ISBN-{random.randint(1, 9999):04d}-{random.randint(1000, 9999)}"
                else:
                    isbn = lib.items[random.randrange(len(lib.items))].isbn
                try:
                    print(
                        f"[STEP {step}] FIND_ISBN isbn='{isbn}' -> 1 items, titles={lib.show_items(isbn, step)}")
                except ValueError as e:
                    print(f'{e}')
            elif act == 'update of index':
                new_index = IndexDict()
                for book in lib.items:
                    new_index.add(book, step)
                lib.index = new_index
                print(f"[STEP {step}] REINDEX -> OK count={len(lib.index)}")
            else:
                try:
                    fake_isbn = '4:44'
                    lib.show_items(fake_isbn, step)
                except ValueError as e:
                    print(f'{e}')
        except ValueError as e:
            print(f'{e}')


def main():
    while True:
        try:
            steps = int(input('Введите количество шагов симуляции: '))
            break
        except ValueError:
            print("ERROR: wrong amount of steps")
    while True:
        try:
            seed = int(input('Введите seed: '))
            if seed == -1:
                seed = None
            break
        except ValueError:
            print("ERROR: wrong seed")
    run_simulation(steps, seed)


if __name__ == "__main__":
    main()
