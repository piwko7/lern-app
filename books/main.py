from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from app.database_connection import SessionLocal
from app.schemas.books import Books


# schemas.books.Base.metadata.create_all(bind=engine)
# app.schemas.books.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_populate_db():
    db = SessionLocal()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(Books).all()
    json_compatible_item_data = jsonable_encoder(books)

    return JSONResponse(status_code=status.HTTP_200_OK, content=json_compatible_item_data)


@app.get("/books/add")
def get_books(db: Session = Depends(get_db)):
    book = {"name": "Bogaty ojciec"}
    db.add(Books(**book))
    db.commit()
    return {"message": f"{book['name']} added succesfully."}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
