import uuid

from app.database import Base
from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()"),
    )
    name = Column(String, nullable=True)
    telegram_id = Column(String, unique=True, index=True)
    display_mode = Column(String, default="normal")
