from fastapi import APIRouter, Depends, HTTPException, status
from app.db import get_session_no_transaction
from app.factory.users import UserFactory
from app.models import User, CreateUser
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[User])
def get_all_users(session: Session = Depends(get_session_no_transaction)):
    return UserFactory(session).get_all()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, session: Session = Depends(get_session_no_transaction)):
    return UserFactory(session).create(user)

@router.get("/{id}", response_model=User)
def get_user_by_id(id: int, session: Session = Depends(get_session_no_transaction)):
    user = UserFactory(session).get_by_id(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/{id}", response_model=User)
def update_user(id: int, user: CreateUser, session: Session = Depends(get_session_no_transaction)):
    user = UserFactory(session).update_by_id(id, user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user