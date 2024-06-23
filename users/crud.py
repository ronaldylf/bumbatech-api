from sqlalchemy.orm import Session
from fastapi import Depends
from users.models.user_model import User
from users.schemas import UserRequest, UserResponse

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserRequest):
    db_user = User(
        **user.model_dump()
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def exists_by_id(db: Session, id: int) -> bool:
    return db.query(User).filter(User.id == id).first() is not None

def exists_by_email(db: Session, email: str) -> bool:
    return db.query(User).filter(User.email == email).first() is not None

def update_user(db: Session, user: User) -> User:
    db.merge(user)
    db.commit()
    return user

def delete_user(db: Session, user: User) -> User:
    db.delete(user)
    db.commit()
    return user