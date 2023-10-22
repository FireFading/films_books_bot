import uuid

from app.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class UserFilm(Base):
    __tablename__ = "users_films"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()"),
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    film_id = Column(UUID(as_uuid=True), ForeignKey("films.id"), nullable=False)

    comment = Column(Text, nullable=True)
    is_done = Column(Boolean, default=False)
    rating = Column(Integer, nullable=True)

    film = relationship("Film", lazy="joined", backref="user_films")
