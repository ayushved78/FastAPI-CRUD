"""Main module."""

from fastapi import FastAPI,Body
from data.new_book import New_Books

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
    author: str
    country: str
    imageLink: str
    language: str
    pages: int
    title: str
    year: int
    description: str
    rating: float


if __name__ == '__main__':
    print(123)


