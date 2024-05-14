from fastapi import FastAPI
from api.main import api
from core.db.engine import init_superadmin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(api, prefix='/api')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_superadmin()