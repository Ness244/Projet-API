from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from core.db.models import Base, User, Syslog
from core.security import get_password_hash
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

def init_superadmin():
    session = sessionmaker(autoflush=False, bind=engine)()

    is_admin = session.query(User).filter(User.is_superuser == True).first()
    if is_admin:
        return True

    default_password = get_password_hash('admin')
    admin_obj = {
        "full_name": "Administrator",
        "username":"admin",
        "is_superuser": True,
        "password": default_password
    }
    admin_obj = User(**admin_obj)
    session.add(admin_obj)
    session.commit()
    session.refresh(admin_obj)

    return admin_obj