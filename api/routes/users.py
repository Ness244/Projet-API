from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from api.models import UserCreate, UserDelete, UserLogin, UserUpdate, UserBase, UsersOut
from core.db.engine import SessionDep
from core.db.models import User
from core.security import get_password_hash, generate_access_token, verify_password, oauth2_scheme, validate_token

router = APIRouter()


@router.get("", response_model=UsersOut)
def get_users(session: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):
    validate_token(token)
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
def update_user(session: SessionDep, user_in: UserUpdate, token: Annotated[str, Depends(oauth2_scheme)]):
    validate_token(token)
    if user_in.password:
        user_in.password = get_password_hash(user_in.password)
    
    user = session.query(User).filter(User.username == user_in.username).first()
    if not user :
        raise HTTPException(
            status_code = 404,
            detail      = f"User with username {user_in.username} is not in database"
        )
    count = -1 # Username will be replaced by the same username
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
def delete_user(session: SessionDep, user_in: UserDelete, token: Annotated[str, Depends(oauth2_scheme)]):
    validate_token(token)
    user_obj = session.query(User).filter(User.username == user_in.username).first()
    if not user_obj:
        raise HTTPException(
            status_code = 404,
            detail      = f"User with username {user_in.username} is not in database"
        )
    if user_obj.is_superuser : # type: ignore
        raise HTTPException(
            status_code = 403,
            detail      = f"Forbidden : cannot delete a super user, demote it first"
        )
    session.query(User).filter(User.id == user_obj.id).delete() 
    session.commit()
    return JSONResponse(
        status_code = 200, 
        content     = {"message": f"User {user_in.username} deleted successfully."}
    )


@router.post("/login")
def login(session: SessionDep, user_in: UserLogin):
    user = session.query(User).filter(User.username == user_in.username).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="Invalid credentials"
        )
    if not verify_password(user_in.password, user.password):
        raise HTTPException(
            status_code=403,
            detail="Invalid credentials"
        )

    token = generate_access_token(data=user.username)

    return JSONResponse(
        status_code=200,
        content={"access_token": token}
    )