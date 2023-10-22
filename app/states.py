from aiogram.fsm.state import State, StatesGroup


class UserRegisterStates(StatesGroup):
    NAME = State()


class FilmAddStates(StatesGroup):
    TITLE = State()
    COMMENT = State()


class FilmGetStates(StatesGroup):
    FILTER = State()