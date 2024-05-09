from fastapi import APIRouter
from api.models import UserCreate, UserDelete, UserIn

router = APIRouter()

@router.post("/")
def create_user(user_in: UserCreate):
   ... 

@router.patch("/")
def update_user(user_in: UserIn):
    ...

@router.post("/login")
def login(user_in: UserCreate):
    ...