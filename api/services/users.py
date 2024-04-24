from models.user import User
from datetime import datetime
from databases.db_user import DBUser
from sqlalchemy.orm import Session
from sqlalchemy import or_

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