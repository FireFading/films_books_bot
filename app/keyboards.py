from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from app.config import Constants, film_filters

cancel_button = KeyboardButton(text=Constants.CANCEL)


def get_only_cancel_markup() -> ReplyKeyboardMarkup | None:
    builder = ReplyKeyboardBuilder()
    builder.add(cancel_button)
    builder.adjust(1)
    return builder.as_markup()

def get_films_filter_markup() -> ReplyKeyboardMarkup | None:
    builder = ReplyKeyboardBuilder()
    for button in film_filters.keys():
        builder.button(text=button)
    builder.add(cancel_button)
    builder.adjust(len(film_filters), 1)
    return builder.as_markup()
