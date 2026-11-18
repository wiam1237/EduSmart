# Plateforme intelligente de productivité étudiante

Plateforme web pour l'analyse, la prédiction et l'amélioration de la
productivité des étudiants, avec un assistant conversationnel branché
sur les résultats réels.

Cette version est l'initialisation technique. Elle fournit l'arborescence,
l'API, la page d'accueil, PostgreSQL et Docker. Elle ne contient ni jeu de
données, ni modèle entraîné, ni tableau de bord métier.

Le dépôt se clone tel quel. Le dossier local peut s'appeler autrement
que le nom du dépôt : tous les chemins partent de la racine du projet.

## Arborescence

```text
backend/          API FastAPI, configuration, PostgreSQL, tests
frontend/         Application React (Vite)
data/raw          CSV déposés à la main (train, test, sample_submission)
data/processed    Jeux préparés, non versionnés
notebooks/        Analyse exploratoire
src/              Traitement, analyses, modèles, SHAP, recommandations
models/           Futurs modèles sauvegardés, non versionnés
docs/             Traçabilité du cahier des charges
```

Deux rôles sont prévus : administrateur et étudiant.

La correspondance exigence par exigence est dans
[docs/CAHIER_DES_CHARGES_MAPPING.md](docs/CAHIER_DES_CHARGES_MAPPING.md).

## Choix techniques

- Python 3.12 est la version de référence (image Docker). Le code reste
  compatible avec Python 3.13 pour un poste qui ne dispose pas encore de 3.12.
- Les chemins Python passent par `pathlib`.
- Les fins de ligne du dépôt sont LF (`.gitattributes`), y compris sur Windows.
- Les dépendances Data Science sont à la racine. L'image de l'API ne les
  installe pas tant que la prédiction n'est pas branchée.
- PostgreSQL est le stockage des comptes et du futur historique.
  Les CSV Kaggle restent des fichiers : ils ne décrivent pas le suivi
  réel des utilisateurs.
- Les prédictions devront être affichées comme des estimations.
- L'assistant aura un fournisseur interchangeable (API ou modèle open source)
  et ne sera appelé qu'avec un contexte issu des données stockées.
- Docker Desktop suffit sur Apple Silicon et sur Windows : les images
  `python:3.12-slim`, `node:22-alpine` et `postgres:16-alpine` existent
  en ARM64 et en AMD64. Aucune plateforme n'est forcée.
- Docker n'est pas obligatoire pour l'API et React. Il est le moyen le plus
  simple d'obtenir le même PostgreSQL sur les deux systèmes.

## Prérequis

Communs aux deux postes :

- Git
- Python 3.12
- Node.js 22 LTS (Node.js 20 ou plus récent convient)
- Docker Desktop, pour PostgreSQL ou pour toute la pile

### macOS (Apple Silicon)

```bash
brew install python@3.12 node@22 libomp
brew install --cask docker
```

`libomp` est nécessaire pour charger XGBoost sur macOS. L'API, elle, n'en a pas besoin.

Python.org et Node.js.org conviennent aussi. Ouvrir Docker Desktop une fois
avant `docker compose`.

### Windows 10 ou 11

1. Installer [Python 3.12](https://www.python.org/downloads/windows/) en cochant **Add python.exe to PATH**.
2. Installer [Node.js 22 LTS](https://nodejs.org/).
3. Installer [Git for Windows](https://git-scm.com/download/win).
4. Installer [Docker Desktop](https://www.docker.com/products/docker-desktop/) et le laisser démarré.
5. Si XGBoost ne se charge pas, installer le [redistribuable Microsoft Visual C++](https://learn.microsoft.com/fr-fr/cpp/windows/latest-supported-vc-redist) (2015-2022).

Dans PowerShell, si l'activation de l'environnement virtuel est bloquée :

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Configuration

À la racine du dépôt.

macOS :

```bash
cp .env.example .env
```

Windows (PowerShell) :

```powershell
Copy-Item .env.example .env
```

Changer `POSTGRES_PASSWORD`, puis reporter le même mot de passe dans
`DATABASE_URL`. Éviter les caractères réservés dans une URL (`@`, `:`, `/`).
Le fichier `.env` reste local.

## Démarrage sur macOS

Terminal 1, PostgreSQL :

```bash
docker compose up postgres -d
```

Terminal 2, Python, à la racine :

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -r backend/requirements.txt
cd backend
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

Terminal 3, frontend :

```bash
cd frontend
npm ci
npm run dev
```

## Démarrage sur Windows

PowerShell 1 :

```powershell
docker compose up postgres -d
```

PowerShell 2, à la racine :

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -r backend\requirements.txt
cd backend
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

PowerShell 3 :

```powershell
cd frontend
npm ci
npm run dev
```

## Vérifier

- API : http://127.0.0.1:8001/api/health
- Documentation interactive : http://127.0.0.1:8001/docs
- Interface : http://127.0.0.1:5173

La page affiche l'état renvoyé par l'API. `database` vaut `up` lorsque
PostgreSQL accepte la connexion, et `down` lorsqu'il est arrêté. Ce second
cas n'empêche pas l'API de répondre.

Le proxy de développement appelle `127.0.0.1` et non `localhost`.
Sur macOS, `localhost` peut viser une autre adresse IPv6 déjà occupée.

Tests :

```bash
cd backend
python -m pytest
```

Sous Windows, la même commande fonctionne dans l'environnement virtuel activé.

## Tout lancer avec Docker

Docker Desktop doit être démarré. À la racine :

```bash
docker compose up --build
```

La commande est la même sur macOS et Windows.
L'API est publiée sur le port 8001 et l'interface sur le port 5173.
Dans Compose, l'API parle à PostgreSQL par le nom `postgres`, même si
`.env` contient `127.0.0.1` pour un lancement hors Docker.

Arrêt :

```bash
docker compose down
```

Les données PostgreSQL restent dans le volume `postgres_data`.
Pour supprimer aussi ce volume : `docker compose down -v`.

## Si un port est déjà pris

PostgreSQL est publié sur le port 5433 et l'API sur le port 8001, car 5432
et 8000 sont souvent déjà utilisés. À l'intérieur de Docker, PostgreSQL
écoute toujours sur 5432 et l'API sur 8000.

Si 5433 ou 8001 sont eux aussi occupés, changer `POSTGRES_PORT` ou
`BACKEND_PORT` dans `.env`, et le port de `DATABASE_URL` pour un lancement
hors Docker. Le proxy Vite local doit alors viser le même port que l'API.

## Notebook

Après installation des dépendances de la racine et dépôt des trois CSV
dans `data/raw` :

macOS

```bash
source .venv/bin/activate
jupyter lab
```

Windows

```powershell
.\.venv\Scripts\Activate.ps1
jupyter lab
```

Ouvrir `notebooks/01_analyse_exploratoire.ipynb` depuis la racine du dépôt
ou depuis `notebooks/`. Le notebook signale les fichiers absents et ne
fabrique pas de résultat à leur place.

## Ce qui n'est pas encore développé

- Comptes, authentification et écrans administrateur ou étudiant.
- Lecture, nettoyage et indicateurs du jeu de données.
- Entraînement, comparaison, explicabilité et recommandations.
- Formulaire de prédiction et historique.
- Dialogue avec un modèle de langage.

La prochaine phase est l'étude du dataset et l'analyse exploratoire.
