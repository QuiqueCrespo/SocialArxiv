from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=True)
    orcid = Column(String(255), nullable=True)
    is_verified = Column(Integer, default=0)  # 0 = not verified, 1 = verified
    created_at = Column(DateTime, default=datetime.utcnow)
    papers = relationship('Paper', back_populates='author')

class Paper(Base):
    __tablename__ = 'papers'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    abstract = Column(Text, nullable=False)
    authors = Column(String(255), nullable=False)  # Comma-separated for now
    tags = Column(String(255), nullable=True)      # Comma-separated for now
    channel = Column(String(255), nullable=False)
    pdf_url = Column(String(255), nullable=True)
    date = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='papers') 