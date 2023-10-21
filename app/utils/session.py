from functools import wraps

from app.database import async_session


def with_async_session(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            kwargs["session"] = session
            return await func(*args, **kwargs)

    return wrapper
