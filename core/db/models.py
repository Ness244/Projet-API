from sqlalchemy import Column, String, Text, Boolean, DateTime, Integer, SmallInteger, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id           = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name    = Column(String(255), nullable=True)
    username     = Column(String(255), unique=True, index=True, nullable=False)
    email        = Column(String(255), nullable=True)
    is_superuser = Column(Boolean, default=False)
    password     = Column(String(255), nullable=False)


class Syslog(Base):
    """
    Not a real syslog implementation, but heavily borrowed from 
    https://datatracker.ietf.org/doc/html/rfc5424#section-6
    """
    __tablename__ = 'syslogs'

    id          = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    severity    = Column(SmallInteger, nullable=False, index=True)
    hostname    = Column(String(255), nullable=True, index=True)
    app_name    = Column(String(48), nullable=True, index=True)
    proc_id     = Column(String(128), nullable=True, index=True)
    msg_id      = Column(String(32), nullable=True)
    timestamp   = Column(DateTime, nullable=True)
    msg         = Column(Text, nullable=False)