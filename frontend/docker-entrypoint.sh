#!/bin/sh
set -eu

# Le volume nommé masque node_modules au premier démarrage.
# npm ci s'exécute dans le conteneur Linux, de la même façon sur macOS et Windows.
if [ ! -d node_modules/react ]; then
  echo "Installation des dépendances npm dans le conteneur..."
  npm ci
fi

exec npm run dev -- --host 0.0.0.0 --port 5173
