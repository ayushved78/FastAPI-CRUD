"""Main module."""

from fastapi import FastAPI,Body
from data.new_book import New_Books
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def first_route():
    return {"message":"Route to /book for more information!"}
@app.get("/book")
async def read_book():
    return New_Books
@app.post("/book/create_book_without_validation")
async def create_book_without_validation(no_validation=Body()):
    New_Books.append(no_validation) 
    return {"message":"Book added to the record withut validation!"}

class BookDataAPI:
    id: int
    author: str
    country: str
    imageLink: str
    language: str
    pages: int
    title: str
    year: int
    description: str
    rating: float

    def __init__(self, id, author, country, imageLink, language, pages, title, year, description, rating):
        self.id = id
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.pages = pages
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    author: str = Field(min_length=1)
    country: str
    imageLink: str
    language: str = Field(min_length=3)
    pages: int = Field(gt=50,lt=1500) 
    title: str = Field(min_length=3)
    year: int
    description: str = Field(min_length=1,max_length=100)
    rating: float = Field(gt=-1,lt=6)

@app.post("/book/create_book")
async def create_book(book_request: BookRequest):
    print(type(book_request))
    # convert the BookDataAPI type to dcit before moving as a new book
    new_book = BookDataAPI(**book_request.dict())
    New_Books.append(new_book)

if __name__ == '__main__':
    print(123)


