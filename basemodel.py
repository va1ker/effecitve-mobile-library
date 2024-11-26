import os
import json

from settings import JSON_NAME

class BaseModel:
    _id_counter = 0  # Общий счетчик для ID
    _file_path = JSON_NAME  # Файл для хранения всех объектов

    def __init__(self):
        BaseModel._id_counter += 1
        self.id = BaseModel._id_counter

    @classmethod
    def _load_all(cls):
        """Загрузка всех данных из файла."""
        if not os.path.exists(cls._file_path):
            return []
        with open(cls._file_path, 'r') as f:
            return json.load(f)

    @classmethod
    def _save_all(cls, data):
        """Сохранение всех данных в файл."""
        with open(cls._file_path, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def save(self):
        """Сохранение текущего объекта."""
        data = self._load_all()
        # Проверка, существует ли объект с таким ID
        for obj in data:
            if obj['id'] == self.id:
                raise ValueError(f"Объект с id={self.id} уже существует.")
        # Сохранение нового объекта
        data.append(self.__dict__)
        self._save_all(data)

    @classmethod
    def get(cls, **kwargs):
        """Поиск объектов по ключам."""
        data = cls._load_all()
        results = []
        for obj in data:
            if all(obj.get(key) == value for key, value in kwargs.items()):
                results.append(obj)
        return results

    def update(self, **kwargs):
        """Обновление объекта, кроме ID."""
        data = self._load_all()
        for obj in data:
            if obj['id'] == self.id:
                for key, value in kwargs.items():
                    if key != "id":  # Игнорируем изменения ID
                        obj[key] = value
                self._save_all(data)
                return
        raise ValueError(f"Объект с id={self.id} не найден.")

    @classmethod
    def delete(cls, obj_id):
        """Удаление объекта по ID."""
        data = cls._load_all()
        updated_data = [obj for obj in data if obj['id'] != obj_id]
        if len(data) == len(updated_data):
            raise ValueError(f"Объект с id={obj_id} не найден.")
        cls._save_all(updated_data)

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"