from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

if not settings.is_local:
    engine = create_engine(settings.postgres_url, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    if not settings.is_local:
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
