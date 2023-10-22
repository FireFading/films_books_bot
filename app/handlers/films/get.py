from aiogram import types
from aiogram.fsm.context import FSMContext
from app.config import Answers, film_filters
from app.controllers.films import film_controller
from app.exceptions.users import UserNotFound
from app.keyboards import get_only_cancel_markup, get_films_filter_markup
from app.states import FilmGetStates
from app.utils.cancel import check_canceled_action



async def get_films(message: types.Message, state: FSMContext):
    await state.set_state(FilmGetStates.FILTER)
    markup = get_films_filter_markup()
    await message.answer(Answers.GET_FILM_FILTER, reply_markup=markup)


@check_canceled_action
async def filter_films(message: types.Message, state: FSMContext):
    markup = types.ReplyKeyboardRemove()
    filters = film_filters.get(message.text)
    films = await film_controller.get_films(filters=filters, telegram_id=str(message.from_user.id))
    await state.clear()
    await message.answer("\n".join([film.display() for film in films]), reply_markup=markup)