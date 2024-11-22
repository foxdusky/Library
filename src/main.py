from library import Library


def main():
    library = Library()

    while True:
        print("\n--- Библиотека ---")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            library.add_book(title, author, year)
            print("Книга добавлена!")

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            if library.remove_book(book_id):
                print("Книга удалена.")
            else:
                print("Книга не найдена.")

        elif choice == "3":
            title = input("Название (оставьте пустым для пропуска): ")
            author = input("Автор (оставьте пустым для пропуска): ")
            year = input("Год (оставьте пустым для пропуска): ")
            year = int(year) if year else None
            results = library.search_books(title, author, year)
            for book in results:
                print(book.to_dict())

        elif choice == "4":
            for book in library.list_books():
                print(book.to_dict())

        elif choice == "5":
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            if library.update_status(book_id, new_status):
                print("Статус обновлен.")
            else:
                print("Книга не найдена.")

        elif choice == "6":
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите еще раз.")


if __name__ == "__main__":
    main()
