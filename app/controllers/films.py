from app.exceptions.users import UserNotFound
from app.services.films import FilmService, film_service
from app.services.users import UserService, user_service
from app.services.users_films import UserFilmService, user_film_service
from app.utils.session import with_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.films import Film as FilmModel


class FilmController:
    def __init__(
        self,
        user_service: UserService,
        film_service: FilmService,
        user_film_service: UserFilmService,
    ):
        self.user_service = user_service
        self.film_service = film_service
        self.user_film_service = user_film_service

    @with_async_session
    async def add_film(
        self,
        telegram_id: str,
        title: str,
        comment: str,
        session: AsyncSession | None = None,
    ):
        user = await self.user_service.get(telegram_id=telegram_id, session=session)
        if not user:
            raise UserNotFound()
        film = await self.film_service.get_or_create(title=title, session=session)
        return await self.user_film_service.update_or_create(
            film_id=film.id, comment=comment, user_id=user.id, session=session
        )

    @with_async_session
    async def get_films(self, telegram_id: str, filters: dict, session: AsyncSession) -> list[FilmModel]:
        user = await self.user_service.get(telegram_id=telegram_id, session=session)
        if not user:
            raise UserNotFound()
        user_films = await self.user_film_service.get_films(user_id=user.id, filters=filters, session=session)
        return [user_film.film for user_film in user_films]


film_controller = FilmController(
    user_service=user_service,
    film_service=film_service,
    user_film_service=user_film_service,
)
