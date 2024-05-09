from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.models import SyslogIn, SyslogCreate, SyslogsOut, SyslogBase
from core.db.engine import SessionDep
from core.db.models import Syslog

router = APIRouter()


@router.get("", response_model=SyslogsOut)
def get_syslog(session: SessionDep, syslog_in: SyslogIn):
    # We add the filters only if they are not null
    filters = {k: v for k, v in syslog_in.model_dump().items() if v is not None}
    results = session.query(Syslog).filter_by(**filters).all()

    # We have to perfom conversion of db model to data model
    data_payload =  [ SyslogBase.model_validate(syslog_obj.__dict__) for syslog_obj in results ]
    return SyslogsOut(
        data = data_payload,
        count = len(data_payload)
    )

@router.post("")
def create_syslog(session: SessionDep, syslog_in: SyslogCreate):
    syslog_obj = Syslog(**syslog_in.model_dump())
    session.add(syslog_obj)
    session.commit()
    session.refresh(syslog_obj)

    return JSONResponse(status_code=201, content={"message": "Syslog entry created successfully", "syslog_id": syslog_obj.id})


@router.delete("")
def delete_syslog(session: SessionDep, syslog_in: SyslogIn):
    # We add the filters only if they are not null
    filters = {k: v for k, v in syslog_in.model_dump().items() if v is not None}
    results = session.query(Syslog).filter_by(**filters).delete()
    session.commit()

    return JSONResponse(status_code=200, content={"message": f"Deleted {results} entries"})