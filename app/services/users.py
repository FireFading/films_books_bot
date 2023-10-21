from app.models.users import User as UserModel
from app.repositories.users import UserRepository, user_repository
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def get(self, telegram_id: str, session: AsyncSession) -> UserModel | None:
        return await self.user_repository.get(telegram_id=telegram_id, session=session)

    async def create(self, telegram_id: str, name: str, session: AsyncSession) -> UserModel:
        user = UserModel(telegram_id=telegram_id, name=name)
        return await self.user_repository.create(instance=user, session=session)


user_service = UserService(user_repository=user_repository)
