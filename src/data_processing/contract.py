"""Contrat des fichiers sources et des étapes de préparation.

Le téléchargement du jeu Kaggle n'est pas automatisé.
Les fichiers doivent être déposés manuellement dans data/raw.
"""

from pathlib import Path

from src.paths import project_root

EXPECTED_RAW_FILES = ("train.csv", "test.csv", "sample_submission.csv")

PIPELINE_STEPS = (
    "import_train_test_sample_submission",
    "exploration_validation",
    "missing_values",
    "duplicates",
    "outliers",
    "categorical_encoding",
    "numeric_normalization",
    "train_evaluation_split",
    "store_processed",
)


def raw_directory() -> Path:
    return project_root() / "data" / "raw"


def processed_directory() -> Path:
    return project_root() / "data" / "processed"


def inspect_raw_files() -> dict[str, bool]:
    """Indique, pour chaque fichier attendu, s'il est réellement présent."""
    directory = raw_directory()
    return {name: (directory / name).is_file() for name in EXPECTED_RAW_FILES}
