from datetime import datetime

from models.user import User, UserLogin
from security.sessions import create_user_session

from sqlalchemy import or_, and_
from sqlalchemy.orm import Session
from databases.db_user import DBUser



def create_account(user: User, db: Session):
    existing_user = db.query(DBUser).filter(or_(DBUser.username ==  user.username, DBUser.email == user.email)).first()
    if existing_user:
        return {"message": "Error: account username/email already exists"}

    db_user = DBUser(first_name=user.first_name, last_name=user.last_name,
                        email=user.email, username=user.username, 
                        password=user.password, created_at=datetime.now())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User account created"}

def login(credentials: UserLogin, db: Session):
    user = db.query(DBUser).filter(and_(DBUser.password == credentials.password, 
                                    or_(DBUser.username == credentials.username, 
                                    DBUser.email == credentials.username))).first()
    if not user:
        return {"message": "Incorrect username or password"}
    
    session_token = create_user_session(user, db)

    return {"message": "Successfully logged in!", "session": session_token}