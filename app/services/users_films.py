from uuid import UUID

from app.models.users_films import UserFilm as UserFilmModel
from app.repositories.users_films import UserFilmRepository, user_film_repository
from sqlalchemy.ext.asyncio import AsyncSession


class UserFilmService:
    def __init__(self, user_film_repository: UserFilmRepository) -> None:
        self.user_film_repository = user_film_repository

    async def update_or_create(
        self,
        film_id: UUID,
        user_id: UUID,
        session: AsyncSession,
        comment: str | None = None,
    ) -> UserFilmModel:
        instance = UserFilmModel(user_id=user_id, film_id=film_id)
        user_film = await self.user_film_repository.get(user_id=user_id, film_id=film_id, session=session)
        if not user_film:
            instance.comment = comment
            return await self.user_film_repository.create(instance=instance, session=session)
        if user_film.comment:
            user_film.comment += comment + "\n"
        else:
            user_film.comment = comment + "\n"
        return await self.user_film_repository.update(instance=user_film, session=session)

    async def get_films(self, user_id: UUID, filters: dict, session: AsyncSession) -> list[UserFilmModel] | None:
        return await self.user_film_repository.filter(user_id=user_id, session=session, **filters,)


user_film_service = UserFilmService(user_film_repository=user_film_repository)
