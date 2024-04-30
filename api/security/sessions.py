import secrets
from datetime import datetime, timedelta

from models.user import User

from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from databases.db_session import DBSession


def generate_token():
    return secrets.token_hex(32)

def create_user_session(user: User, db: Session):
    session_token = generate_token()
    while True:
        existing_session = db.query(DBSession).filter(DBSession.token == session_token).first()
        if not existing_session:
            break
        session_token = generate_token()

    current_date = datetime.now()
    expiration_date = current_date + timedelta(minutes=30)
    session = DBSession(token=session_token, user_id=user.id, created_at=current_date, expiration=expiration_date)
    
    db.add(session)
    db.commit()
    db.refresh(session)

    return session_token
            

        