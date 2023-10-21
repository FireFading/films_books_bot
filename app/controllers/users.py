from app.exceptions.users import UserAlreadyExists
from app.models.users import User as UserModel
from app.services.users import UserService, user_service
from app.utils.session import with_async_session
from sqlalchemy.ext.asyncio import AsyncSession


class UserController:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    @with_async_session
    async def register(self, telegram_id: str, name: str, session: AsyncSession | None) -> UserModel:
        if await self.is_register(telegram_id=telegram_id, session=session):
            raise UserAlreadyExists()
        return await self.user_service.create(telegram_id=telegram_id, name=name, session=session)

    @with_async_session
    async def is_register(self, telegram_id: str, session: AsyncSession | None) -> bool:
        user = await self.user_service.get(telegram_id=telegram_id, session=session)
        return bool(user)


user_controller = UserController(user_service=user_service)
