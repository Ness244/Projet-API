from fastapi import APIRouter
from api.routes import syslogs, users

api = APIRouter()
api.include_router(syslogs.router, prefix='/syslog')
api.include_router(users.router, prefix='/user')