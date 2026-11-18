"""Session SQLAlchemy et contrôle de disponibilité de PostgreSQL."""

import logging

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

logger = logging.getLogger("pfa.database")

engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_database() -> str:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception as exc:
        logger.warning(
            "PostgreSQL indisponible lors du contrôle de santé (%s).",
            exc.__class__.__name__,
        )
        return "down"
    return "up"
