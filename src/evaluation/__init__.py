"""Évaluation des modèles par MAE, MSE, RMSE et R².

Les métriques ne seront calculées qu'à partir d'un jeu d'évaluation réel.
"""

from src.machine_learning.registry import EVALUATION_METRICS

__all__ = ["EVALUATION_METRICS"]
