"""Racine Python du dépôt, résolue sans chemin absolu propre à un système."""

from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]
