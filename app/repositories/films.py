from app.models.films import Film as FilmModel
from app.repositories.base import BaseRepository


class FilmRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=FilmModel)


film_repository = FilmRepository()
