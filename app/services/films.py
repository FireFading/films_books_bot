from app.models.films import Film as FilmModel
from app.repositories.films import FilmRepository, film_repository
from sqlalchemy.ext.asyncio import AsyncSession


class FilmService:
    def __init__(self, film_repository: FilmRepository) -> None:
        self.film_repository = film_repository

    async def get_or_create(self, title: str, session: AsyncSession) -> FilmModel:
        film = FilmModel(title=title)
        return await self.film_repository.get_or_create(instance=film, session=session)

    async def create(self, title: str, comment: str, session: AsyncSession) -> FilmModel:
        pass

    # async def


film_service = FilmService(film_repository=film_repository)
