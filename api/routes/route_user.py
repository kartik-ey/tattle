from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.schemas import CreateUser
from database.database import get_db


router = APIRouter()


@router.post('/create_user')
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

