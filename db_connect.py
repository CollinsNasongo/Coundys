import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from config import DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME
# SQLAlchemy engine creation

encoded_password = urllib.parse.quote_plus(DATABASE_PASSWORD)
SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{encoded_password}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URI 
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Function to get a database session
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()