from app.config import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(settings.database_url, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()
