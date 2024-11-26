class BaseModel:
    _id_counter = 0 

    def __init__(self):
        BaseModel._id_counter += 1
        self.id = BaseModel._id_counter

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"

class Book(BaseModel):
    def __init__(self, title, author, year, status=True):
        super().__init__()
        self.title = title 
        self.author = author
        self.year = year
        self.status = status 

    def __repr__(self):
        status_text = "в наличии" if self.status else "выдана"
        return f"<Book id={self.id}, title='{self.title}', author='{self.author}', year={self.year}, status={status_text}>"


