# Cahier des charges — matrice de traçabilité

Ce document relie chaque exigence au module qui la prendra en charge.
L'initialisation prépare les emplacements et les contrats. Elle n'implémente
pas encore les traitements, les modèles ni les écrans métier.

Statuts utilisés :

- **Prêt** : élément utilisable dès cette étape.
- **Préparé** : emplacement, contrat ou règle fixé, implémentation à venir.
- **Hors étape** : explicitement reporté, sans simulation de résultat.

Les prédictions futures seront des estimations. Le jeu Kaggle
(`train.csv`, `test.csv`, `sample_submission.csv`) sert à l'entraînement
et à l'évaluation. Les saisies des utilisateurs et leur historique
seront stockés à part, dans PostgreSQL. Le jeu Kaggle ne sera pas présenté
comme un suivi longitudinal.

## Plateforme

| Exigence | Module | Composants | Validation prévue | Statut |
| --- | --- | --- | --- | --- |
| Collecter et gérer les données étudiants | Data | `src/data_processing/`, futur service `backend/app/services/data` | Les trois CSV sont lus depuis `data/raw` ; les jeux préparés sont écrits dans `data/processed` | Préparé |
| Analyser habitudes et comportements | Data Science | `src/exploratory_analysis/` | Les analyses listées plus bas s'appuient sur les colonnes réellement présentes | Préparé |
| Prédire un score de productivité | Machine Learning | `src/machine_learning/`, `models/` | Une prédiction individuelle consomme le modèle sauvegardé et un formulaire | Préparé |
| Identifier les facteurs d'influence | Data Science, explicabilité | `src/exploratory_analysis/`, `src/explainability/` | Les facteurs affichés proviennent du calcul, pas d'une liste figée | Préparé |
| Expliquer avec SHAP | Explicabilité | `src/explainability/` | Importance globale et contribution d'une prédiction individuelle | Préparé |
| Recommandations personnalisées | Recommandations | `src/recommendations/` | Chaque conseil est lié à une règle et aux facteurs de l'étudiant | Préparé |
| Tableaux de bord interactifs | Data Science, frontend | indicateurs dans `src/exploratory_analysis/`, futures pages React | Chaque indicateur affiché a une source calculée | Préparé |
| Assistant ancré sur les résultats réels | Assistant | `backend/app/services/assistant/` | Aucune statistique n'est produite si elle n'est pas stockée | Préparé |
| Administration des utilisateurs, des données et du suivi | Administration | rôle `administrateur`, futurs routeurs admin | Un compte administrateur gère les comptes et le jeu ; un étudiant ne le peut pas | Préparé |
| Deux rôles seulement | Authentification | `backend/app/core/roles.py` | L'énumération contient uniquement `administrateur` et `etudiant` | Prêt |

## Module Data

| Exigence | Composants | Validation prévue | Statut |
| --- | --- | --- | --- |
| Import de `train.csv`, `test.csv`, `sample_submission.csv` | `src/data_processing/contract.py`, `data/raw/` | `inspect_raw_files()` reflète la présence réelle des trois fichiers | Prêt pour le contrôle de présence ; lecture pandas hors étape |
| Exploration et validation | `notebooks/01_analyse_exploratoire.ipynb`, `src/exploratory_analysis/` | Le notebook s'arrête sur un état explicite si un fichier manque | Préparé |
| Valeurs manquantes, doublons, valeurs aberrantes | étape du `PIPELINE_STEPS` | Un rapport compte les lignes modifiées ou écartées | Préparé |
| Encodage des variables catégorielles | `src/data_processing/` | Les colonnes catégorielles du fichier réel sont encodées, les autres inchangées dans leur rôle | Préparé |
| Normalisation numérique lorsque nécessaire | `src/data_processing/` | La normalisation est justifiée par le modèle qui la requiert | Préparé |
| Séparation entraînement / évaluation | `src/data_processing/`, `src/machine_learning/` | Le jeu d'évaluation n'est pas réutilisé pour ajuster le modèle | Préparé |
| Stockage des données préparées | `data/processed/` | Les fichiers produits sont ignorés par Git | Préparé |
| Mise à jour par l'administrateur | futur service data et route admin | Un étudiant ne peut pas remplacer le jeu d'entraînement | Préparé |

## Module Data Science

| Exigence | Composants | Validation prévue | Statut |
| --- | --- | --- | --- |
| Distribution des scores de productivité | `PLANNED_ANALYSES` | Graphique calculé sur le fichier présent | Préparé |
| Habitudes d'étude | `PLANNED_ANALYSES` | Idem | Préparé |
| Influence du sommeil | `PLANNED_ANALYSES` | Idem | Préparé |
| Utilisation des appareils numériques | `PLANNED_ANALYSES` | Idem | Préparé |
| Relations concentration, stress et productivité | `PLANNED_ANALYSES` | Idem | Préparé |
| Facteurs associés à la productivité | `PLANNED_ANALYSES` | La liste affichée correspond au calcul | Préparé |
| Nombre d'étudiants analysés | `DASHBOARD_INDICATORS` | Compte des lignes réellement chargées | Préparé |
| Score moyen de productivité | `DASHBOARD_INDICATORS` | Moyenne du jeu chargé | Préparé |
| Répartition des niveaux de productivité | `DASHBOARD_INDICATORS` | Effectifs par niveau présent dans les données | Préparé |
| Moyenne des heures d'étude | `DASHBOARD_INDICATORS` | Moyenne de la colonne identifiée dans le fichier | Préparé |
| Moyenne des heures de sommeil | `DASHBOARD_INDICATORS` | Idem | Préparé |
| Répartition des niveaux de concentration | `DASHBOARD_INDICATORS` | Effectifs par niveau | Préparé |
| Facteurs les plus associés | `DASHBOARD_INDICATORS` | Cohérent avec l'analyse ou avec SHAP, selon la phase | Préparé |

Les noms de colonnes ne sont pas figés dans le code : ils seront lus
dans les fichiers déposés.

## Module Machine Learning

| Exigence | Composants | Validation prévue | Statut |
| --- | --- | --- | --- |
| Linear Regression | `CANDIDATE_MODELS` dans `src/machine_learning/registry.py` | Le modèle est entraîné et comparé aux trois autres | Préparé |
| Decision Tree Regressor | idem | idem | Préparé |
| Random Forest Regressor | idem | idem | Préparé |
| XGBoost Regressor | idem, dépendance `xgboost` | idem | Préparé |
| Sélection des variables pertinentes | `src/machine_learning/` | Les variables retenues sont justifiées et enregistrées avec le modèle | Préparé |
| Séparation entraînement / validation | `src/machine_learning/` | Jeu de validation distinct du jeu d'ajustement | Préparé |
| Optimisation des hyperparamètres | `src/machine_learning/` | Grille ou recherche documentée, sans fuite du jeu d'évaluation | Préparé |
| MAE, MSE, RMSE, R² | `src/evaluation/`, `EVALUATION_METRICS` | Les quatre métriques sont produites pour chaque candidat | Préparé |
| Sauvegarde et chargement du meilleur modèle | `models/` | Le fichier rechargé redonne la même prédiction sur un exemple connu | Préparé |
| Prédiction individuelle par formulaire | future route et page étudiant | Le formulaire reprend les variables attendues par le modèle sauvegardé | Préparé |

Aucun modèle n'est entraîné pendant l'initialisation.

## Explicabilité, recommandations et assistant

| Exigence | Composants | Validation prévue | Statut |
| --- | --- | --- | --- |
| Variables les plus influentes globalement | `src/explainability/` | Le graphique SHAP correspond au modèle sauvegardé | Préparé |
| Facteurs d'une prédiction individuelle | `src/explainability/` | Les contributions concernent la saisie de cet étudiant | Préparé |
| Explications compréhensibles | `src/explainability/`, assistant | Le texte reprend les contributions calculées | Préparé |
| Recommandations par règles et facteurs du modèle | `src/recommendations/` | Chaque conseil cite la règle et le facteur qui l'ont déclenché | Préparé |
| Conseils adaptés à l'étudiant | `src/recommendations/` | Deux saisies différentes peuvent produire des conseils différents | Préparé |
| Questions sur la productivité | `CAPABILITIES` | La réponse s'appuie sur un extrait de données disponibles | Préparé |
| Expliquer une prédiction | `CAPABILITIES` | Le texte correspond à l'explication SHAP stockée | Préparé |
| Interpréter les indicateurs | `CAPABILITIES` | Les chiffres cités sont ceux du tableau de bord | Préparé |
| Exploiter SHAP | `CAPABILITIES` | Aucune importance n'est ajoutée hors résultat SHAP | Préparé |
| Conseils personnalisés via l'assistant | `CAPABILITIES` | Les conseils viennent du moteur de règles | Préparé |
| Accès limité aux données réelles | `GROUNDING_RULES`, `LanguageModelProvider` | Le fournisseur reçoit un contexte construit par la plateforme | Préparé |
| Ne pas inventer de scores ni de statistiques | `GROUNDING_RULES` | Si la donnée manque, la réponse le dit | Préparé |
| API LLM ou modèle open source | `backend/app/services/assistant/provider.py` | Un fournisseur peut être branché sans modifier les règles d'ancrage | Préparé |

## Historique et administration

| Exigence | Composants | Validation prévue | Statut |
| --- | --- | --- | --- |
| Conserver les prédictions successives | futur modèle SQLAlchemy d'historique | Chaque prédiction reste consultable après redémarrage | Préparé |
| Historique par étudiant | futur routeur étudiant | Un étudiant ne voit que ses prédictions | Préparé |
| Indicateurs globaux pour l'administrateur | futur routeur admin | Les totaux portent sur les données autorisées à ce rôle | Préparé |
| Gestion des comptes | futur module auth, `UserRole` | Création, consultation et désactivation sans rôle supplémentaire | Préparé |
| Gestion et mise à jour des données | rôle administrateur | Le remplacement du jeu est tracé et réservé à l'administrateur | Préparé |

## Socle technique de cette étape

| Exigence | Composants | Validation | Statut |
| --- | --- | --- | --- |
| API FastAPI | `backend/app/main.py` | `GET /api/health` répond | Prêt |
| Validation Pydantic | `backend/app/schemas/` | Le schéma de santé décrit la réponse | Prêt |
| PostgreSQL et SQLAlchemy | `backend/app/database/`, service Compose | Le champ `database` vaut `up` lorsque PostgreSQL est démarré, `down` sinon | Prêt |
| Configuration et secrets | `backend/app/core/config.py`, `.env.example`, `.gitignore` | `.env` n'est pas versionné | Prêt |
| Journalisation | `backend/app/core/logging.py` | Les erreurs inattendues sont journalisées sans renvoyer la pile au client | Prêt |
| Exceptions | `backend/app/core/exceptions.py` | Une route inconnue reste une erreur 404 | Prêt |
| React, Vite, JavaScript | `frontend/` | La page d'accueil affiche l'état réel de l'API | Prêt |
| Docker Compose multi-architecture | `docker-compose.yml`, Dockerfiles | PostgreSQL, backend et frontend sont définis sans plateforme forcée | Prêt |
| Tests | `backend/tests/` | `python -m pytest` depuis `backend/` | Prêt |
| Chemins portables | `pathlib`, `.gitattributes` | Aucun chemin absolu macOS ou Windows dans le code | Prêt |

## Limites à respecter dans les phases suivantes

- Ne pas présenter une prédiction comme un résultat certain.
- Ne pas mélanger une ligne du jeu Kaggle avec le compte d'un étudiant.
- Ne pas calculer un indicateur de tableau de bord à partir de valeurs inventées.
- Ne pas faire répondre l'assistant lorsqu'aucun résultat stocké ne permet de répondre.
- Ne pas ajouter de rôle technicien.
