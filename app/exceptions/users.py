class UserAlreadyExists(Exception):
    def __init__(self):
        super().__init__("Вы уже зарегистрированы")


class UserNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Пользователь не найден")
