"""Main module."""

from fastapi import FastAPI,Body
from data.Books_data import Books

app = FastAPI()
BOOK = []
@app.get("/book")
async def read_book():
    return Books

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


if __name__ == '__main__':
    print(123)


