from app.models.users import User as UserModel
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=UserModel)


user_repository = UserRepository()
