from typing import Optional
from pydantic import BaseModel


class Transaction(BaseModel):
    id: str
    transaction_date: str
    account_number: str
    sub_account: Optional[str]
    amount_in: float
    amount_out: float
    accumulated: float
    code: Optional[str]
    transaction_content: Optional[str]
    reference_number: Optional[str]
    bank_brand_name: str
    bank_account_id: str 