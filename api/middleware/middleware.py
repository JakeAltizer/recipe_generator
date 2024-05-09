from functools import wraps
from datetime import datetime

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

def get_session_token(request: Request):
    session_token = request.cookies.get("session-token")
    if not session_token:
        raise HTTPException(status_code=404, detail="Session not found")
    return session_token

def get_current_user(request: Request):
    session_token = get_session_token(request)
    db = SessionLocal()

    current_user = db.query(DBUser).filter(DBUser.id == DBSession.user_id,
                                           DBSession.token == session_token,
                                           DBSession.expiration > datetime.now()).first()
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
        session_token = get_session_token(request)
        current_user = get_current_user(request)
        return await handler(request, *args, **kwargs)
    return wrapper