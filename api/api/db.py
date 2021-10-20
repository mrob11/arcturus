import os
from sqlalchemy.engine import create
from sqlmodel import create_engine, SQLModel, Session
from api.config import settings


engine = create_engine(settings.DATABASE_URL, echo=True)


def init_db():
    # SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
