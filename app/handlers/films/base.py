from aiogram import Router
from aiogram.filters import Command, CommandStart
from app.handlers.films.add import add_film, provide_comment, provide_name
from app.handlers.films.get import get_films, filter_films
from app.states import FilmAddStates, FilmGetStates

router = Router(name="films")

router.message.register(add_film, Command("add_film"))
router.message.register(add_film, CommandStart())
router.message.register(provide_name, FilmAddStates.TITLE)
router.message.register(provide_comment, FilmAddStates.COMMENT)

router.message.register(get_films, Command("get_films"))
router.message.register(get_films, CommandStart())
router.message.register(filter_films, FilmGetStates.FILTER)