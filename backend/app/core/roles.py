"""Rôles autorisés. Le cahier des charges ne prévoit pas de rôle technicien."""

from enum import Enum


class UserRole(str, Enum):
    ADMIN = "administrateur"
    STUDENT = "etudiant"
