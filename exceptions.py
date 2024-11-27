class BaseModelError(Exception):
    """
    Base Model Exception, created for correct error handling in models
    """
    pass


class ObjectNotFoundError(BaseModelError):
    def __init__(self, obj_id):
        super().__init__(f"Объект с id={obj_id} не найден.")


class ObjectAlreadyExistsError(BaseModelError):
    def __init__(self, obj_id):
        super().__init__(f"Объект с id={obj_id} уже существует.")