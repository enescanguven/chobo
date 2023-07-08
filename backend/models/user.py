from typing import Optional
from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    email: str
    password: str
    profile_image_link: Optional[str]
    full_name: Optional[str] = None
    display_name: Optional[str] = ""
    country: Optional[str] = ""
    stage: Optional[str] = ""  # What stage are you studying at section at figma
    field: Optional[str] = ""  # I'm studying section in figma


class UserLoginSchema(BaseModel):
    email: str
    password: str


class UserGoogleLoginSchema(BaseModel):
    credential: str


class UserUpdateSchema(BaseModel):
    full_name: Optional[str] = None
    display_name: Optional[str] = None
    stage: Optional[str] = None
    field: Optional[str] = None
    country: Optional[str] = None


class UserPasswordForgotSchema(BaseModel):
    email: str


class UserPasswordResetSchema(BaseModel):
    password: str
    reset_token: str
