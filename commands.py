from typing import Dict, Type, List

from basecommand import BaseCommand
from models import Book


class CommandDispatcher:
    """
    Command dispatcher class, contains dict with key = command input, and value = CommandHandler
    """
    def __init__(self):
        self.commands: Dict[str, Type[BaseCommand]] = {
            "help": HelpCommand,
            "exit": ExitCommand,
            "get_all": GetAllBooksCommand,
            "add": AddBookCommand,
            "update": UpdateBookCommand,
            "delete": DeleteBookCommand,
            "find": FindBooksCommand,
        }

    def dispatch(self, command_name: str):
        """
        Dispatch method simply calls a handle method of CommandHandler
        """
        command_class = self.commands.get(command_name)
        if command_class:
            command = command_class()
            command.handle()
        else:
            print(
                f"Неизвестная команда: {command_name}. Введите 'help' для списка команд."
            )


class ExitCommand(BaseCommand):
    def handle(self) -> None:
        print("Выход из программы. До свидания!")
        exit(0)


class HelpCommand(BaseCommand):
    def handle(self) -> None:
        print("Доступные команды:")
        print("\texit - завершить работу")
        print("\thelp - показать это сообщение")
        print("\tget_all  - показать все книги")
        print("\tfind - найти книгу по title, author или year")
        print("\tadd  - добавить книгу")
        print("\tupdate - обновить информацию о книге по id")
        print("\tdelete - удалить книгу по id")


class GetAllBooksCommand(BaseCommand):
    def handle(self) -> None:
        books: List[Book]  = Book.get_all()
        if books:
            print("Все книги:")
            for book in books:
                print(
                    f"{book.id}: {book.title} — {book.author} ({book.year}) | {'В наличии' if book.status else 'Выдана'}"
                )
        else:
            print("Книг не найдено :(")


class AddBookCommand(BaseCommand):
    def handle(self) -> None:
        title: str = input("Введите название книги: ")
        author: str  = input("Введите автора книги: ")
        year: str = input("Введите год издания книги: ")
        status = (
            input("Введите статус книги (в наличии/выдана): ").strip().lower()
            == "в наличии"
        )

        book = Book(title=title, author=author, year=year, status=status)
        book.save()
        print(f"Книга '{book.title}' была успешно добавлена!")


class FindBooksCommand(BaseCommand):
    def handle(self) -> None:
        args = {}
        print(
            "Введите параметры для поиска книг. Оставьте поле пустым, если параметр не нужен."
        )

        title: str = input("Введите название книги (title): ")
        if title:
            args["title"] = title

        author: str = input("Введите автора книги (author): ")
        if author:
            args["author"] = author

        year: str = input("Введите год издания книги (year): ")
        if year:
            args["year"] = year

        if not args:
            print("Вы не предоставили параметров для поиска :( )")
            return

        books = Book.filter(**args)
        if books:
            for book in books:
                print(
                    f"{book.id}: {book.title} — {book.author} ({book.year}) | {'В наличии' if book.status else 'Выдана'}"
                )
        else:
            print("Книг по таким параметрам не найдено :( )")


class UpdateBookCommand(BaseCommand):
    def handle(self) -> None:
        print(
            "\n Данная команда предназначена для обновления статуса книги(в наличии\выдана)\n"
        )

        command_input: str = input("Введите ID книги для обновления: ")

        book_id: int = int(command_input)

        book = Book.get(id=book_id)
        if book:
            command_input = input("Укажите статус книги(в наличии\выдана): ")
            if command_input == "выдана":
                book.status = False
            elif command_input == "в наличии":
                book.status = True
            book.save()
            print(f"Книга с id {book_id} успешно обновлена.")
        else:
            print(f"Книга с id {book_id} не найдена.")


class DeleteBookCommand(BaseCommand):
    def handle(self) -> None:

        command_input: str = input("Введите ID книги для удаления: ")

        book_id: int  = int(command_input)

        book = Book.get(id=book_id)
        if book:
            book.delete()
            print(f"Книга с id {book_id} успешно удалена.")
        else:
            print(f"Книга с id {book_id} не найдена.")
