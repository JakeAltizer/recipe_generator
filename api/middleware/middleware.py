from functools import wraps
from datetime import datetime

from sqlalchemy import and_
from sqlalchemy.orm import Session
from fastapi import HTTPException, Request

from databases.db_user import DBUser
from databases.db_session import DBSession
from databases.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(session_token: str):
    db = SessionLocal()
    current_user = db.query(DBSession).filter(and_(DBSession.token == session_token, 
                                              DBSession.expiration > datetime.now())).first()
    db.close()

    if not current_user:
        raise HTTPException(status_code=401, 
                            detail="Login session expired. Please login again to continue.")
    return current_user


def authenticate(handler):
    """
    Wrapper function to authenticate users calling
    protected routes.
    """
    @wraps(handler)
    async def wrapper(request: Request, *args, **kwargs):
        session_token = request.cookies.get("session-token")
        current_user = get_current_user(session_token)
        return await handler(request, *args, **kwargs)
    return wrapper