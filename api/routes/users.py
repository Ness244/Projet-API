from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from api.models import UserCreate, UserDelete, UserLogin, UserUpdate, UserBase, UsersOut
from core.db.engine import SessionDep
from core.db.models import User
from core.security import get_password_hash

router = APIRouter()


@router.get("", response_model=UsersOut)
def get_users(session: SessionDep):
    results = session.query(User).all()
    
    # We have to perform conversion of db model to data model
    data_payload = [ UserBase.model_validate(user_obj.__dict__,) for user_obj in results ]
    return UsersOut(
        data  = data_payload,
        count = len(data_payload)
    )


@router.post("")
def create_user(session: SessionDep, user_in: UserCreate):
    result = session.query(User).filter(User.username == user_in.username).first()
    if result:
        raise HTTPException(
            status_code = 403, 
            detail      = f"User {user_in.username} already exists in database"
        ) 
    user_in.password = get_password_hash(user_in.password)
    user_obj = User(**user_in.model_dump())
    session.add(user_obj)
    session.commit()
    session.refresh(user_obj)

    return JSONResponse(
        status_code = 201, 
        content     = {"message": f"User {user_in.username} created successfully."}
    )


@router.patch("")
def update_user(session: SessionDep, user_in: UserUpdate):
    if user_in.password:
        user_in.password = get_password_hash(user_in.password)
    
    user = session.query(User).filter(User.username == user_in.username).first()
    if not user :
        raise HTTPException(
            status_code = 404,
            detail      = f"User with username {user_in.username} is not in database"
        )
    count = 0
    for field, value in user_in:
        if value:
            setattr(user,field,value)
            count+=1
    session.commit()

    return JSONResponse(
        status_code = 200,
        content     = {"message": f"Successfully updated {count} field on {user_in.username}."}
    )


@router.delete("")
def delete_user(session: SessionDep, user_in: UserDelete):
    user_obj = session.query(User).filter(User.username == user_in.username).first()
    if user_obj:
        raise HTTPException(
            status_code = 404,
            detail      = f"User with username {user_in.username} is not in database"
        )
    if user_obj.is_superuser : # type: ignore
        raise HTTPException(
            status_code = 403,
            detail      = f"Forbidden : cannot delete a super user, demote it first"
        )
    
    return JSONResponse(
        status_code = 200, 
        content     = {"message": f"User {user_in.username} deleted successfully."}
    )


@router.post("/login")
def login(session: SessionDep, user_in: UserCreate):
    # TODO: Abou : implemente JWT Token Authentication 
    # TODO: Abou : user auth sur toutes routes, celle ci pour le login et la creation du token
    ...