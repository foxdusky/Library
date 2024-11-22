import json
from book import Book


class Library:
    """Класс для управления библиотекой книг."""

    def __init__(self, filepath: str = "books.json"):
        self.filepath = filepath
        self.books = self.load_books()

    def load_books(self) -> list[Book]:
        """Загружает книги из JSON файла."""
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return [Book.from_dict(book) for book in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        """Сохраняет книги в JSON файл."""
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """Добавляет новую книгу в библиотеку."""
        book_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id: int):
        """Удаляет книгу по ID."""
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def find_book_by_id(self, book_id: int) -> Book | None:
        """Ищет книгу по ID."""
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, title: str = "", author: str = "", year: int = None) -> list[Book]:
        """Поиск книг по названию, автору или году."""
        results = self.books
        if title:
            results = [book for book in results if title.lower() in book.title.lower()]
        if author:
            results = [book for book in results if author.lower() in book.author.lower()]
        if year:
            results = [book for book in results if book.year == year]
        return results

    def list_books(self) -> list[Book]:
        """Возвращает список всех книг."""
        return self.books

    def update_status(self, book_id: int, new_status: str):
        """Обновляет статус книги по ID."""
        book = self.find_book_by_id(book_id)
        if book:
            book.status = new_status
            self.save_books()
            return True
        return False
