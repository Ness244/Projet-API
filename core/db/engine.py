from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from core.db.models import Base, User, Syslog
import config

DATABASE_URL = f"mysql+mysqlconnector://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@{config.DATABASE_HOST}/{config.DATABASE_NAME}"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
SessionGenerator = sessionmaker(autoflush=False, bind=engine)


def get_db():
    db = SessionGenerator()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[Session, Depends(get_db)]