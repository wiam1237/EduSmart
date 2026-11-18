"""Journalisation. Les secrets, dont l'URL de base de données, ne sont pas écrits."""

import logging

from app.core.config import settings

logger = logging.getLogger("pfa")


def configure_logging(level: str | None = None) -> None:
    resolved = (level or settings.log_level).upper()
    logging.basicConfig(
        level=resolved,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        force=True,
    )
    logger.setLevel(resolved)
