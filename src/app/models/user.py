from app.db import SQLBaseModelAudit
from sqlmodel import Field

class User(SQLBaseModelAudit, table=True):
    id: int = Field(default=None, primary_key=True, nullable=False)
    first_name: str | None = Field(default=None, nullable=False)
    last_name: str | None = Field(default=None, nullable=False)