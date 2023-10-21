from aiogram.fsm.state import State, StatesGroup


class UserRegisterStates(StatesGroup):
    NAME = State()
