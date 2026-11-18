"""Point d'extension pour une API LLM ou un modèle open source."""

from typing import Protocol


class LanguageModelProvider(Protocol):
    """Contrat d'un fournisseur de langage.

    `context` devra être construit à partir des données et résultats
    déjà calculés. Un fournisseur ne doit pas être appelé sans ce contexte.
    """

    def complete(self, prompt: str, context: dict[str, object]) -> str:
        """Retourne une réponse conditionnée par le contexte fourni."""
