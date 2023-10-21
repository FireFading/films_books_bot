from app.models.books import Book as BookModel
from app.repositories.base import BaseRepository


class BookRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=BookModel)


book_repository = BookRepository()
