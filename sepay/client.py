from typing import Dict, List, Optional, Union
import requests

from sepay.models.transaction import Transaction
from sepay.models.bank_account import BankAccount

from sepay.api.transactions import TransactionAPI
from sepay.api.bank_accounts import BankAccountAPI
from sepay.api.qr_code import QRCodeAPI





class SePayClient:
    def __init__(self, api_token: str, base_url: str = "https://my.sepay.vn"):
        self.api_token = api_token
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        })

        # Initialize API clients
        self.transactions = TransactionAPI(self.session, self.base_url)
        self.bank_accounts = BankAccountAPI(self.session, self.base_url)
        self.qr_code = QRCodeAPI()

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
        return self.transactions.get_transactions(
            account_number=account_number,
            transaction_date_min=transaction_date_min,
            transaction_date_max=transaction_date_max,
            since_id=since_id,
            limit=limit,
            reference_number=reference_number,
            amount_in=amount_in,
            amount_out=amount_out
        )

    def get_transaction_details(self, transaction_id: str) -> Transaction:
        """Get details of a specific transaction."""
        return self.transactions.get_transaction_details(transaction_id)

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
        return self.bank_accounts.get_bank_accounts(
            short_name=short_name,
            last_transaction_date_min=last_transaction_date_min,
            last_transaction_date_max=last_transaction_date_max,
            since_id=since_id,
            limit=limit,
            accumulated_min=accumulated_min,
            accumulated_max=accumulated_max
        )

    def get_bank_account_details(self, bank_account_id: str) -> BankAccount:
        """Get details of a specific bank account."""
        return self.bank_accounts.get_bank_account_details(bank_account_id)

    def generate_qr_code(
        self,
        account_number: str,
        bank_name: str,
        amount: Optional[float] = None,
        description: Optional[str] = None
    ) -> str:
        """Generate QR code URL for payment."""
        return self.qr_code.generate_qr_code(
            account_number=account_number,
            bank_name=bank_name,
            amount=amount,
            description=description
        ) 