import uuid

from app.database import Base
from sqlalchemy import Column, Date, Float, LargeBinary, String, text
from sqlalchemy.dialects.postgresql import UUID


class Book(Base):
    __tablename__ = "books"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()"),
    )
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    publication_date = Column(Date)
    genre = Column(String(50))
    description = Column(String(500))
    price = Column(Float, nullable=False)
    pdf = Column(LargeBinary)
    rating = Column(Float)
