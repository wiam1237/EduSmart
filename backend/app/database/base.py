"""Base déclarative SQLAlchemy, partagée par les futurs modèles."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
