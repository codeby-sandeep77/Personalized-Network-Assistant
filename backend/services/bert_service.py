"""DistilBERT theme extraction service."""

from typing import Any


class BertService:
    """Extract themes and keywords from event descriptions using DistilBERT."""

    def __init__(self) -> None:
        self._model = None
        self._tokenizer = None

    def _load_model(self) -> None:
        """Lazy-load the DistilBERT model and tokenizer."""
        if self._model is None:
            from transformers import AutoModelForSequenceClassification, AutoTokenizer

            model_name = "distilbert-base-uncased"
            self._tokenizer = AutoTokenizer.from_pretrained(model_name)
            self._model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def extract_themes(self, text: str) -> dict[str, Any]:
        """Extract themes and ranked keywords from the given text."""
        # Placeholder — full implementation in Epic 3
        return {
            "themes": [],
            "keywords": [],
            "message": "Theme extraction will be implemented in Epic 3",
        }


bert_service = BertService()
