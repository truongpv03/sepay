from typing import List, Optional
import requests
from sepay.models.bank_account import BankAccount


class BankAccountAPI:
    def __init__(self, session: requests.Session, base_url: str):
        self.session = session
        self.base_url = base_url

    def get_bank_accounts(
        self,
        short_name: Optional[str] = None,
        last_transaction_date_min: Optional[str] = None,
        last_transaction_date_max: Optional[str] = None,
        since_id: Optional[str] = None,
        limit: int = 100,
        accumulated_min: Optional[float] = None,
        accumulated_max: Optional[float] = None
    ) -> List[BankAccount]:
        """Get list of bank accounts with optional filters."""
        params = {
            "short_name": short_name,
            "last_transaction_date_min": last_transaction_date_min,
            "last_transaction_date_max": last_transaction_date_max,
            "since_id": since_id,
            "limit": limit,
            "accumulated_min": accumulated_min,
            "accumulated_max": accumulated_max
        }
        params = {k: v for k, v in params.items() if v is not None}

        response = self.session.get(
            f"{self.base_url}/userapi/bankaccounts/list",
            params=params
        )
        response.raise_for_status()
        data = response.json()
        return [BankAccount(**b) for b in data["bankaccounts"]]

    def get_bank_account_details(self, bank_account_id: str) -> BankAccount:
        """Get details of a specific bank account."""
        response = self.session.get(
            f"{self.base_url}/userapi/bankaccounts/details/{bank_account_id}"
        )
        response.raise_for_status()
        data = response.json()
        return BankAccount(**data["bankaccount"])