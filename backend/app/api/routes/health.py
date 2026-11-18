"""Contrôle de disponibilité de l'API et de PostgreSQL."""

from fastapi import APIRouter

from app.database.session import check_database
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="pfa-student-productivity-api",
        database=check_database(),
    )
