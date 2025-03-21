from typing import List, Optional
import requests
from sepay.models.transaction import Transaction


class TransactionAPI:
    def __init__(self, session: requests.Session, base_url: str):
        self.session = session
        self.base_url = base_url

    def get_transactions(
        self,
        account_number: Optional[str] = None,
        transaction_date_min: Optional[str] = None,
        transaction_date_max: Optional[str] = None,
        since_id: Optional[str] = None,
        limit: int = 5000,
        reference_number: Optional[str] = None,
        amount_in: Optional[float] = None,
        amount_out: Optional[float] = None
    ) -> List[Transaction]:
        """Get list of transactions with optional filters."""
        params = {
            "account_number": account_number,
            "transaction_date_min": transaction_date_min,
            "transaction_date_max": transaction_date_max,
            "since_id": since_id,
            "limit": limit,
            "reference_number": reference_number,
            "amount_in": amount_in,
            "amount_out": amount_out
        }
        params = {k: v for k, v in params.items() if v is not None}

        response = self.session.get(
            f"{self.base_url}/userapi/transactions/list",
            params=params
        )
        response.raise_for_status()
        data = response.json()
        return [Transaction(**t) for t in data["transactions"]]

    def get_transaction_details(self, transaction_id: str) -> Transaction:
        """Get details of a specific transaction."""
        response = self.session.get(
            f"{self.base_url}/userapi/transactions/details/{transaction_id}"
        )
        response.raise_for_status()
        data = response.json()
        return Transaction(**data["transaction"]) 