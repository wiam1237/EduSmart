"""Registre des routes.

Routes prévues, non exposées tant que les modules ne sont pas implémentés :
authentification, utilisateurs, données, analyses, prédictions,
explications SHAP, recommandations, assistant et administration.
"""

from fastapi import APIRouter

from app.api.routes import health

api_router = APIRouter()
api_router.include_router(health.router)
