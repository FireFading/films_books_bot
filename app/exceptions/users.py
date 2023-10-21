class UserAlreadyExists(Exception):
    def __init__(self):
        super().__init__("Вы уже зарегистрированы")
