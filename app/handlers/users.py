from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from app.config import Answers
from app.controllers.users import user_controller
from app.exceptions.users import UserAlreadyExists
from app.keyboards import get_only_cancel_markup
from app.states import UserRegisterStates
from app.utils.cancel import check_canceled_action

router = Router(name="users")


@router.message(Command("register"))
@router.message(CommandStart())
async def register(message: types.Message, state: FSMContext):
    await state.set_state(UserRegisterStates.NAME)
    markup = get_only_cancel_markup()
    await message.answer(Answers.GET_NAME, reply_markup=markup)


@router.message(UserRegisterStates.NAME)
@check_canceled_action
async def provide_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    markup = types.ReplyKeyboardRemove()
    await state.clear()
    try:
        await user_controller.register(telegram_id=str(message.from_user.id), name=name, session=None)
        await message.answer(Answers.REGISTRATION_SUCCESS, reply_markup=markup)
    except UserAlreadyExists:
        await message.answer(Answers.USER_ALREADY_EXISTS, reply_markup=markup)
