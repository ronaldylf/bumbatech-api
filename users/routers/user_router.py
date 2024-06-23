from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Union, Annotated
from sqlalchemy.orm import Session
from shared.dependencies import get_db
from users.models.user_model import User
from users.schemas import UserRequest, UserResponse
from users import crud

router = APIRouter(prefix="/users")

@router.post("/create-user", response_model=UserResponse, status_code=201)
def create_user(new_user_request: UserRequest,
                  db: Session = Depends(get_db)) -> UserResponse:

    if not crud.exists_by_email(email=new_user_request.email, db=db):
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.create_user(db=db, user=new_user_request)


@router.get("/", response_model=List[UserResponse])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[UserResponse]:
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    db_user = crud.get_user(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/update-user", response_model=UserResponse)
def update_user(updated_user: UserResponse, db: Session = Depends(get_db)) -> UserResponse:
    db_user = crud.get_user(user_id=updated_user.id, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.update_user(db=db, user=User(**updated_user.model_dump()))


@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    db_user = crud.get_user(user_id=user_id, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.delete_user(user=db_user, db=db)
