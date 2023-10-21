from functools import wraps

from aiogram import types
from aiogram.fsm.context import FSMContext
from app.config import Answers, Constants


def check_canceled_action(func):
    @wraps(func)
    async def wrapper(message: types.Message, state: FSMContext, *args, **kwargs):
        if message.text == Constants.CANCEL:
            await state.clear()
            markup = types.ReplyKeyboardRemove()
            return await message.answer(Answers.CANCEL_ACTION, reply_markup=markup)
        return await func(message, state, *args, **kwargs)

    return wrapper
