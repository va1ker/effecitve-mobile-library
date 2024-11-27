import os
import json

from settings import JSON_NAME
from commands import CommandDispatcher


def healthcheck() -> None:
    """
    check's if .json exist, if not, create it
    """
    if not os.path.exists(JSON_NAME):
        print(f"Файл {JSON_NAME} не найден. Создаю новый.")
        with open(JSON_NAME, "w", encoding="utf8") as f:
            json.dump([], f, indent=4)
    else:
        print(f"Файл {JSON_NAME} уже существует.")



def main() -> None:
    """
    Main func of all program, initilizing dispatcher and run programm in infinite loop,
    """
    healthcheck()

    print(
        "Вас приветствует система управления библиотекой книг っ◔◡◔)っ ♥\n",
        "Используйте help для того чтобы увидеть все доступные команды\n",
    )

    dispatcher = CommandDispatcher()

    while True:
        command_input = input("Введите команду: ").strip().lower()
        command_name = command_input 

        if not command_name:
            print("Команда не может быть пустой.")
            continue

        dispatcher.dispatch(command_name)


if __name__ == "__main__":
    main()
