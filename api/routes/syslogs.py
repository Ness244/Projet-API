from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from api.models import SyslogIn, SyslogCreate, SyslogsOut, SyslogBase
from core.db.engine import SessionDep
from core.db.models import Syslog, User
from core.security import oauth2_scheme, validate_token, get_current_user

router = APIRouter()


@router.get("", response_model=SyslogsOut)
def get_syslog(session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)], syslog_in: SyslogIn = None ):
    validate_token(token)
    # We add the filters only if they are not null
    if  syslog_in:
        filters = {k: v for k, v in syslog_in.model_dump().items() if v is not None}
        results = session.query(Syslog).filter_by(**filters).all()
    else:

        results = session.query(Syslog).all()
    # We have to perfom conversion of db model to data model
    data_payload =  [ SyslogBase.model_validate(syslog_obj.__dict__) for syslog_obj in results ]
    return SyslogsOut(
        data = data_payload,
        count = len(data_payload)
    )

@router.post("")
def create_syslog(session: SessionDep, syslog_in: SyslogCreate, token: Annotated[str, Depends(oauth2_scheme)]):
    validate_token(token)
    current_user = get_current_user(token)
    syslog_in.msg += f" - created by {current_user}"
    syslog_obj = Syslog(**syslog_in.model_dump())
    session.add(syslog_obj)
    session.commit()
    session.refresh(syslog_obj)

    return JSONResponse(status_code=201, content={"message": "Syslog entry created successfully", "syslog_id": syslog_obj.id})


@router.delete("")
def delete_syslog(session: SessionDep, syslog_in: SyslogIn, token: Annotated[str, Depends(oauth2_scheme)]):
    validate_token(token)
    user_name = get_current_user(token)
    user = session.query(User).filter(User.username == user_name).first()
    if not user:
        raise HTTPException(status_code=403, detail="Access denied")

    if not user.is_superuser:
        raise HTTPException(status_code=403, detail="Forbidden : you are not a super user")

    # We add the filters only if they are not null
    filters = {k: v for k, v in syslog_in.model_dump().items() if v is not None}
    results = session.query(Syslog).filter_by(**filters).delete()
    session.commit()

    return JSONResponse(status_code=200, content={"message": f"Deleted {results} entries"})
