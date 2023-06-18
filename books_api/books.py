from fastapi import Body, FastAPI
from data.Books_data import Books

app = FastAPI()

@app.get("/")
async def first_api():
    return {'message':'Hello Ayush!'}

@app.get("/books-data")
async def read_books():
    return Books

# dynamic parameters
@app.get("/books-data/{book_title}")
async def specific_book(book_title: str):
    for book in Books:
        # check if the searched book and requested book matches
        if book.get('title').casefold() == book_title.casefold():
            return book

# query parameters
@app.get("/books-data/{b_author}/")
async def readBook_by_language(b_author: str, b_language: str):
    book_by_lang = []
    for book in Books:
        if book.get('author').casefold() == b_author.casefold() and \
        book.get('language').casefold() == b_language.casefold():
            book_by_lang.append(book)
        
    return book_by_lang

# POST Request Method
"""
{
    "author": "",
    "country": "",
    "imageLink": "",
    "language": "",
    "link": "",
    "pages": ,
    "title": "",
    "year": 
}
"""

@app.post("/books-data/create_book")
async def create_book(new_book = Body()):
    Books.append(new_book)

# PUT Request Method
@app.put("/ooks-data/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == updated_book.get('title').casefold():
            Books[i] = updated_book
    
    return {'message':'value updated!'}

# DELETE Request Method
@app.delete("/books-data/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == book_title.casefold():
            Books.pop(i)
            return {'message':'value deleted successfully!'}
        else:
            return {'message':'failed to delete book!'}
        
# Fetch all books of specific author
@app.get("/books-data/by_author/")
async def fetch_allBooks_author(book_author: str):
    books_by_author = []
    for book in Books:
        if book.get('author').casefold() == book_author.casefold():
            books_by_author.append(book)
    return books_by_author