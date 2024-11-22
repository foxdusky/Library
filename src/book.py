class Book:
    """Класс для представления книги в библиотеке."""

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """Возвращает словарь с данными книги для сохранения в JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Создает экземпляр книги из словаря."""
        return cls(data["id"], data["title"], data["author"], data["year"], data["status"])
