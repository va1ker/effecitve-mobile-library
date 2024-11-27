from basemodel import BaseModel

class Book(BaseModel):
    def __init__(self, title:str, author:str, year:str, status: bool = True):
        super().__init__()
        self.title: str = title 
        self.author: str = author
        self.year: str = year
        self.status: bool = status 

    def __repr__(self):
        status_text = "в наличии" if self.status else "выдана"
        return f"<Book id={self.id}, title='{self.title}', author='{self.author}', year={self.year}, status={status_text}>"


