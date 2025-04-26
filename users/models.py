from sqlalchemy import Boolean, Column, Integer, String
from auth.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(16), unique=True, index=True)
    hashed_password = Column(String(256))
    is_active = Column(Boolean, default=True)
