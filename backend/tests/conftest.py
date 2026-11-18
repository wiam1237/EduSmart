"""Rend la racine du dépôt et le paquet backend importables pendant les tests."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "backend"

for path in (str(ROOT), str(BACKEND)):
    if path not in sys.path:
        sys.path.insert(0, path)
