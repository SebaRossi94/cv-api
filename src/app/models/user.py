from app.db import SQLBaseModelAudit, SQLBaseModel
from sqlmodel import Field

class UserBase(SQLBaseModel):
    first_name: str | None = Field(default=None, nullable=False)
    last_name: str | None = Field(default=None, nullable=False)


class User(UserBase, SQLBaseModelAudit, table=True):
    id: int = Field(default=None, primary_key=True, nullable=False)

class CreateUser(UserBase):
    pass