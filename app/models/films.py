import uuid

from app.database import Base
from sqlalchemy import Column, Date, Float, String, Text, text
from sqlalchemy.dialects.postgresql import UUID


class Film(Base):
    __tablename__ = "films"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()"),
    )
    title = Column(String(255), nullable=False, unique=True)
    release_date = Column(Date, nullable=True)
    genre = Column(String(50), nullable=True)
    director = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    rating = Column(Float, nullable=True)

    def display(self):
        return (
            f"Название: {self.title}\n"
            + self.pretty_release_date
            + self.pretty_genre
            + self.pretty_director
            + self.pretty_description
            + self.pretty_rating
        )

    @property
    def pretty_release_date(self) -> str:
        return (
            f"Дата выхода: {self.release_date.strftime('%d.%m.%Y')}\n"
            if self.release_date
            else ""
        )

    @property
    def pretty_genre(self) -> str:
        return f"Жанр: {self.genre}\n" if self.genre else ""

    @property
    def pretty_director(self) -> str:
        return f"Режиссёр: {self.director}\n" if self.director else ""

    @property
    def pretty_description(self) -> str:
        return f"Описание: {self.description}\n" if self.description else ""

    @property
    def pretty_rating(self) -> str:
        return f"Рейтинг: {self.rating}\n" if self.rating else ""
