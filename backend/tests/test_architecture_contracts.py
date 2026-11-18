"""Garde-fous d'architecture : le cahier des charges reste visible dans le code."""

from app.core.roles import UserRole
from app.services.assistant import CAPABILITIES, GROUNDING_RULES
from src.data_processing.contract import EXPECTED_RAW_FILES, PIPELINE_STEPS
from src.exploratory_analysis import DASHBOARD_INDICATORS, PLANNED_ANALYSES
from src.machine_learning.registry import CANDIDATE_MODELS, EVALUATION_METRICS


def test_only_admin_and_student_roles_exist() -> None:
    assert {role.value for role in UserRole} == {"administrateur", "etudiant"}


def test_kaggle_files_expected_by_the_specification() -> None:
    assert EXPECTED_RAW_FILES == ("train.csv", "test.csv", "sample_submission.csv")


def test_data_pipeline_covers_the_specified_steps() -> None:
    assert "missing_values" in PIPELINE_STEPS
    assert "duplicates" in PIPELINE_STEPS
    assert "outliers" in PIPELINE_STEPS
    assert "categorical_encoding" in PIPELINE_STEPS
    assert "numeric_normalization" in PIPELINE_STEPS
    assert "train_evaluation_split" in PIPELINE_STEPS
    assert "store_processed" in PIPELINE_STEPS


def test_planned_analyses_and_dashboard_indicators() -> None:
    assert "distribution_scores_productivite" in PLANNED_ANALYSES
    assert "influence_sommeil" in PLANNED_ANALYSES
    assert "nombre_etudiants_analyses" in DASHBOARD_INDICATORS
    assert "facteurs_les_plus_associes" in DASHBOARD_INDICATORS


def test_models_and_metrics_match_the_specification() -> None:
    assert CANDIDATE_MODELS == (
        "linear_regression",
        "decision_tree_regressor",
        "random_forest_regressor",
        "xgboost_regressor",
    )
    assert EVALUATION_METRICS == ("mae", "mse", "rmse", "r2")


def test_assistant_stays_grounded_on_real_results() -> None:
    assert "exploitation_shap" in CAPABILITIES
    assert "ne_pas_inventer_de_scores_ou_de_statistiques" in GROUNDING_RULES
    assert "separer_le_jeu_kaggle_des_saisies_utilisateur" in GROUNDING_RULES
