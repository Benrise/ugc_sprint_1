from datetime import datetime, timedelta
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field
from core.config import settings


class UserCreate(BaseModel):
    login: str = Field(min_length=4, max_length=255)
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class UserInDB(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserInDBRole(UserInDB):
    role_id: int


class UserRoles(BaseModel):
    user: int = 1
    admin: int = 2
    superuser: int = 3


class UserEmailLogin(BaseModel):
    email: EmailStr
    password: str


class UsernameLogin(BaseModel):
    username: str
    password: str


class LoginHistory(BaseModel):
    user_id: UUID
    #logged_at: datetime


class UserHistoryInDB(BaseModel):
    id: UUID
    user_id: UUID
    logged_at: datetime


class JTWSettings(BaseModel):
    authjwt_secret_key: str = settings.secret_key_session
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: set = {"access", "refresh"}
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_csrf_protect: bool = False
    access_expires: timedelta = timedelta(minutes=1)
    refresh_expires: timedelta = timedelta(days=30)


class TokensResponse(BaseModel):
    access_token: str
    refresh_token: str


class ChangeUsername(BaseModel):
    new_username: str


class ChangePassword(BaseModel):
    new_password: str


class OAuthData(BaseModel):
    user_id: str
    email: str | None
