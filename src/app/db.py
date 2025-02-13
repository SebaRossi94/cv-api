from datetime import datetime, timezone
from sqlmodel import SQLModel, Session
from sqlalchemy import create_engine
from sqlmodel import Field
from sqlalchemy import event, DateTime, Column
from app.settings import settings


DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True, pool_size=20, max_overflow=20)


class SQLBaseModel(SQLModel):
    pass


class SQLBaseModelAudit(SQLBaseModel):
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
        ),
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
        ),
    )


@event.listens_for(SQLBaseModelAudit, "before_update", propagate=True)
def updated_at(mapper, connection, target):
    target.updated_at = datetime.now(timezone.utc)


def get_session():
    with Session(engine, autoflush=True) as session:
        with session.begin():
            yield session


def get_session_no_transaction():
    with Session(engine) as session:
        yield session
