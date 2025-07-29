from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str] = None
    orcid: Optional[str] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: Optional[str]
    orcid: Optional[str]
    is_verified: int
    created_at: datetime

    class Config:
        orm_mode = True

class PaperCreate(BaseModel):
    title: str
    abstract: str
    authors: str
    tags: Optional[str] = None
    channel: str
    pdf_url: Optional[str] = None

class PaperOut(BaseModel):
    id: int
    title: str
    abstract: str
    authors: str
    tags: Optional[str]
    channel: str
    pdf_url: Optional[str]
    date: datetime
    author_id: int

    class Config:
        orm_mode = True 