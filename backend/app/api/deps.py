"""Dépendances FastAPI réutilisables par les futurs routeurs."""

from app.database.session import get_db

__all__ = ["get_db"]
