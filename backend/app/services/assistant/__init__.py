"""Assistant conversationnel ancré sur les résultats réels de la plateforme.

Aucune réponse n'est générée à cette étape.
"""

CAPABILITIES = (
    "questions_productivite",
    "explication_prediction_individuelle",
    "interpretation_indicateurs",
    "exploitation_shap",
    "conseils_personnalises",
)

GROUNDING_RULES = (
    "utiliser_uniquement_les_donnees_et_resultats_disponibles",
    "ne_pas_inventer_de_scores_ou_de_statistiques",
    "presenter_les_predictions_comme_des_estimations",
    "separer_le_jeu_kaggle_des_saisies_utilisateur",
)
