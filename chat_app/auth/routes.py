from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .dependencies import get_db, authenticate_user, get_user
from .models import Token
from .schemas import UserCreate, UserResponse
from users.models import User
from .utils import get_password_hash, create_access_token


router = APIRouter()  # Add a prefix to the auth routes


@router.post('/token', response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "bearer"}
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/signup', response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
