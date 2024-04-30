import os
import hmac
import hashlib

from pydantic import BaseModel, validator

SECRET_KEY = os.environ['AUTH_KEY'].encode("utf-8")

class UserBase(BaseModel):
    username: str
    password: str

    @validator("password")
    def hash_password(cls, v):
        return hmac.new(SECRET_KEY, v.encode(), hashlib.sha256).hexdigest()


class User(UserBase):
    first_name: str
    last_name: str
    email: str

class UserLogin(UserBase):
    pass
