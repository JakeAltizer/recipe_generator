from pydantic import BaseModel, validator
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str

    @validator("password")
    def hash_password(cls, v):
        return pwd_context.hash(v)