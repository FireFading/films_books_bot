from app.models.users_books import UserBook as UserBookModel
from app.repositories.base import BaseRepository


class UserBookRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=UserBookModel)


user_book_repository = UserBookRepository()
