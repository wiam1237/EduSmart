"""Modèles et métriques imposés par le cahier des charges.

La sélection de variables, la séparation entraînement/validation,
l'optimisation des hyperparamètres, la sauvegarde du meilleur modèle
et la prédiction individuelle seront ajoutées ici.
Les artefacts iront dans le dossier models/ à la racine du dépôt.
"""

CANDIDATE_MODELS = (
    "linear_regression",
    "decision_tree_regressor",
    "random_forest_regressor",
    "xgboost_regressor",
)

EVALUATION_METRICS = ("mae", "mse", "rmse", "r2")
