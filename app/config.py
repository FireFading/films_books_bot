from app.settings import Settings


class Constants:
    CANCEL = "Отменить"


class Answers:
    CANCEL_ACTION = "Действие отменено"
    GET_NAME = "Введите имя"
    REGISTRATION_SUCCESS = "Регистрация прошла успешно"
    USER_ALREADY_EXISTS = "Вы уже зарегистрированы"
    USER_NOT_FOUND = "Пользователь не найден"

    GET_FILM_TITLE = "Введите название фильма"
    GET_FILM_COMMENT = "Введите комментарий к фильму"
    GET_FILM_FILTER = "Выберите фильтр"
    FILM_ADDED = "Фильм добавлен"


film_filters = {
    "Все": {},
    "Непросмотренные": {"is_done": False},
    "Просмотренные": {"is_done", True},
}
settings = Settings()
