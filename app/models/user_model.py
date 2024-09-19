from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)

    owner = relationship("User", back_populates="items")
"""
September 17, 2024
Daily Update
-------------

A. R&D on Advanced FastAPI topic:
    1. SQLAlchemy.
    2. Pydantic schemas.

"""