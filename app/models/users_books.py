import uuid

from app.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text, text
from sqlalchemy.dialects.postgresql import UUID


class UserBook(Base):
    __tablename__ = "users_books"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()"),
    )
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    book_id = Column(UUID(as_uuid=True), ForeignKey("books.id"), nullable=False)

    comment = Column(Text)
    is_done = Column(Boolean)
    rating = Column(Integer)
