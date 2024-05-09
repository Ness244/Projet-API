from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
# FastAPI DATA models here


class UserBase(BaseModel):
    """Base User format, closest to DB Model"""
    
    # The following makes sure we do not add unwanted field such as 
    # password when performing object conversion
    model_config = ConfigDict(extra='ignore')
    
    full_name       : str | None = None
    username        : str # ID
    email           : str | None = None
    is_superuser    : bool = False


class UserCreate(UserBase):
    """Format used when creating new user entry"""
    username: str
    password: str
class UserUpdate(UserBase):
    """Format used when updating user entry"""
    username: str
    password: str

class UserLogin(UserBase):
    """Format used when tryng to update user"""
    username: str
    password: str

class UserDelete(BaseModel):
    """Format used when deleting user"""
    username: str

class UsersOut(BaseModel):
    """Format used when sending back users"""
    data: list[UserBase]
    count: int

class SyslogBase(BaseModel):
    """Base syslog format, closest to DB model"""
    id: int
    severity    : int = Field(ge=0, le=7)
    hostname    : str | None = None
    app_name    : str | None = None
    proc_id     : str | None = None
    msg_id      : str | None = None
    timestamp   : datetime | None = None
    msg         : str


class SyslogIn(BaseModel):
    """Format used when querying syslog entries"""
    severity    : int | None = None
    hostname    : str | None = None
    app_name    : str | None = None



class SyslogsOut(BaseModel):
    """Format used when sending back syslog entries"""
    data: list[SyslogBase]
    count: int

class SyslogCreate(BaseModel):
    """Format used when creating new syslog entry"""
    severity    : int = Field(ge=0, le=7)
    hostname    : str | None = None
    app_name    : str | None = None
    proc_id     : str | None = None
    msg_id      : str | None = None
    timestamp   : datetime | None = None
    msg         : str