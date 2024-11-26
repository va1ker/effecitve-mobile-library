from basemodel import BaseModel

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


