from fastapi import APIRouter, HTTPException, status
from app.dependencies.db import session_no_transaction_dependency
from app.factory.users import UserFactory
from app.models import User, CreateUser
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[User])
def get_all_users(session: Session = session_no_transaction_dependency):
    return UserFactory(session).get_all()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, session: Session = session_no_transaction_dependency):
    return UserFactory(session).create(user)

@router.get("/{id}", response_model=User)
def get_user_by_id(id: int, session: Session = session_no_transaction_dependency):
    user = UserFactory(session).get_by_id(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/{id}", response_model=User)
def update_user(id: int, user: CreateUser, session: Session = session_no_transaction_dependency):
    user = UserFactory(session).update_by_id(id, user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user