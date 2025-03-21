from typing import Callable, Dict, Optional
import json
from sepay.models.webhook import WebhookTransaction


class WebhookHandler:
    def __init__(self, secret: Optional[str] = None):
        self.secret = secret
        self._transaction_handlers: Dict[str, Callable] = {}

    def on_transaction(self, handler: Callable[[WebhookTransaction], None]):
        """Register a handler for transaction webhooks."""
        self._transaction_handlers["transaction"] = handler

    def handle(self, payload: str) -> Dict:
        """Handle incoming webhook payload."""
        try:
            data = json.loads(payload)
            if not isinstance(data, dict):
                return {"success": False, "message": "Invalid payload format"}

            # Verify webhook signature if secret is provided
            if self.secret:
                # TODO: Implement signature verification
                pass

            # Handle transaction webhook
            if "gateway" in data and "transactionDate" in data:
                transaction = WebhookTransaction(**data)
                if "transaction" in self._transaction_handlers:
                    self._transaction_handlers["transaction"](transaction)
                return {"success": True}

            return {"success": False, "message": "Unknown webhook type"}

        except json.JSONDecodeError:
            return {"success": False, "message": "Invalid JSON payload"}
        except Exception as e:
            return {"success": False, "message": str(e)} 