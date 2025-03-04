from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.schemas import Book, BookUpdateModel
from src.db.main import get_session
from src.books.services import BookService
from src.books.models import Book

book_router = APIRouter()
book_service = BookService()


# returns all books
@book_router.get("/", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = book_service.get_all_books(session)
    return books


# create a book
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book(
    book_data: Book, session: AsyncSession = Depends(get_session)
) -> dict:
    new_book = book_service.create_book(book_data, session)
    return new_book


# returns book by id
@book_router.get("/{book_id}")
async def get_book(book_id: int, session: AsyncSession = Depends(get_session)) -> dict:
    book = book_service.get_book(book_id, session)
    if book:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# update details of a book
@book_router.patch("/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language

            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Book is not found"
    )


# delete a book
@book_router.delete("/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book Deleted Successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
