from fastapi import FastAPI
from app.authors.router import router as router_authors
from app.books.router import router as router_books
from app.borrows.router import router as router_borrow



app = FastAPI()



@app.get('/')
def read_root():
    return {'message': 'main'}



app.include_router(router_authors)
app.include_router(router_books)
app.include_router(router_borrow)