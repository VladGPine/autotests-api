import uuid

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(UserSchema):
    """
    Описание структуры запроса на создание пользователя с паролем.
    """
    password: str


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
