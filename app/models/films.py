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
    name = Column(String, nullable=True)
    title = Column(String(255), nullable=False)
    release_date = Column(Date)
    genre = Column(String(50))
    director = Column(String(255))
    description = Column(Text)
    rating = Column(Float)
