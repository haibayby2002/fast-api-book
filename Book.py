from pydantic import BaseModel, Field

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    def __init__ (self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description 
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=5)