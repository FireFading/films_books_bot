from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from app.config import Answers
from app.controllers.films import film_controller
from app.exceptions.users import UserNotFound
from app.keyboards import get_only_cancel_markup
from app.states import FilmAddStates
from app.utils.cancel import check_canceled_action

router = Router(name="films")


@router.message(Command("add-film"))
@router.message(CommandStart())
async def add_film(message: types.Message, state: FSMContext):
    await state.set_state(FilmAddStates.TITLE)
    markup = get_only_cancel_markup()
    await message.answer(Answers.GET_FILM_TITLE, reply_markup=markup)


@router.message(FilmAddStates.TITLE)
@check_canceled_action
async def provide_name(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(FilmAddStates.COMMENT)
    markup = get_only_cancel_markup()
    await message.answer(Answers.GET_FILM_COMMENT, reply_markup=markup)


@router.message(FilmAddStates.COMMENT)
@check_canceled_action
async def provide_comment(message: types.Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()
    markup = types.ReplyKeyboardRemove()
    await state.clear()
    try:
        await film_controller.add_film(**data, telegram_id=str(message.from_user.id))
        await message.answer(Answers.FILM_ADDED, reply_markup=markup)
    except UserNotFound:
        await message.answer(Answers.USER_NOT_FOUND, reply_markup=markup)
