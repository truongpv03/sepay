from pydantic import BaseModel


class BankAccount(BaseModel):
    id: str
    account_holder_name: str
    account_number: str
    accumulated: float
    last_transaction: str
    label: str
    active: str
    created_at: str
    bank_short_name: str
    bank_full_name: str
    bank_bin: str
    bank_code: str 