from app.models.users_films import UserFilm as UserFilmModel
from app.repositories.base import BaseRepository


class UserFilmRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=UserFilmModel)


user_film_repository = UserFilmRepository()
