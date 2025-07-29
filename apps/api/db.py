from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from packages.db.models import Base

DATABASE_URL = "mysql+pymysql://socialarxiv_user:password@localhost/socialarxiv"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine) 