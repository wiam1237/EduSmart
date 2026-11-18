# Données

Ce dossier sépare le jeu utilisé pour entraîner et évaluer les modèles
des résultats calculés ensuite.

## `raw/`

Fichiers à déposer manuellement, sans téléchargement automatique :

- `train.csv`
- `test.csv`
- `sample_submission.csv`

Ils servent à l'exploration, à l'entraînement et à l'évaluation.
Ils ne constituent pas un suivi longitudinal des utilisateurs de la plateforme.

## `processed/`

Jeux préparés par le futur pipeline : valeurs manquantes, doublons,
valeurs aberrantes, encodage, normalisation et séparation
entraînement / évaluation.

Les fichiers déposés ici ne sont pas versionnés.
Les prédictions saisies par les étudiants seront stockées dans PostgreSQL,
pas dans ces CSV.
