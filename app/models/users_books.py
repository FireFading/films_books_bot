import uuid

from app.database import Base
from sqlalchemy import Column, ForeignKey, text
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
    book_id = Column(ForeignKey("books.id"), UUID(as_uuid=True), nullable=False)
