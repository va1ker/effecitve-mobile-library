import os
import json
from typing import List, Any, TypeVar, Type

from settings import JSON_NAME
from exceptions import ObjectAlreadyExistsError, ObjectNotFoundError

T = TypeVar("T", bound="BaseModel") # Annotation thing

class BaseModel:
    """
    BaseModel class represents a model, and any model should inherit from it
    Contains base logic for ID counting and CRUD operations
    Returns a BaseModel objects
    """
    _id_counter = 0
    _file_path = JSON_NAME
    _cached_data = None

    def __init__(self):
        if BaseModel._cached_data is None:
            BaseModel._cached_data = self._load_all()

        # If there would be already some data in data.json, will take the last object id and put it in counter
        if BaseModel._cached_data:
            BaseModel._id_counter = int(BaseModel._cached_data[-1]["id"]) + 1 
        else:
            BaseModel._id_counter += 1

        self.id = BaseModel._id_counter

    @classmethod
    def _load_all(cls) -> Any :
        """Load all data from JSON file"""
        if not os.path.exists(cls._file_path):
            return []
        with open(cls._file_path, "r", encoding="utf8") as f:
            return json.load(f)

    @classmethod
    def _save_all(cls, data) -> None:
        """Save data to file"""
        with open(cls._file_path, "w", encoding="utf8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @classmethod
    def _create_object_from_data(cls: Type[T], data: dict) -> T:
        """Simple serializer that return a Model object instead of dict"""
        obj = cls.__new__(cls)
        obj.__dict__.update(data)
        return obj

    @classmethod
    def get(cls: Type[T], obj_id: int) -> T | ObjectNotFoundError:
        """Find object by it's ID"""
        data = cls._load_all()
        for obj_data in data:
            if int(obj_data["id"]) == obj_id:
                return cls._create_object_from_data(obj_data)
        raise ObjectNotFoundError(obj_id)

    def save(self) -> None | ObjectAlreadyExistsError:
        """Save object to JSON"""

        data = self._load_all()
        for obj in data:
            if obj["id"] == self.id:
                raise ObjectAlreadyExistsError(self.id)

        BaseModel._cached_data.append(self.__dict__)
        self._save_all(BaseModel._cached_data)

    @classmethod
    def get_all(cls: Type[T]) -> List[T]:
        """Get all objects """
        data = cls._load_all()
        return [cls._create_object_from_data(obj) for obj in data]

    @classmethod
    def filter(cls: Type[T], **kwargs) -> List[T]:
        """
        Filters objects by matching query
        Goes through all object and searching for match by using all()
        """
        data = cls._load_all()
        results = []
        for obj in data:
            if all(
                value.lower() in str(obj.get(key, "")).lower()
                for key, value in kwargs.items()
            ):
                results.append(cls._create_object_from_data(obj))
        return results

    def delete(self) -> None:
        data = self._load_all()
        updated_data = [obj for obj in data if obj["id"] != self.id]
        if len(updated_data) == len(data):
            raise ObjectNotFoundError(self.id)

        self._save_all(updated_data)

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
