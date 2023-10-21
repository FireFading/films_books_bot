from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from app.config import Constants

cancel_button = KeyboardButton(text=Constants.CANCEL)


def get_only_cancel_markup() -> ReplyKeyboardMarkup | None:
    builder = ReplyKeyboardBuilder()
    builder.add(cancel_button)
    return builder.as_markup()
