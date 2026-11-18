"""Point d'entrée de l'API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.api.router import api_router
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import configure_logging

configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=__version__,
    description=(
        "API de la plateforme d'analyse, de prédiction et d'amélioration "
        "de la productivité des étudiants."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"],
)

register_exception_handlers(app)
app.include_router(api_router, prefix="/api")
