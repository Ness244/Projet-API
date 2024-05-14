from fastapi import FastAPI
from api.main import api
from core.db.engine import init_superadmin

app = FastAPI()
app.include_router(api, prefix='/api')

init_superadmin()