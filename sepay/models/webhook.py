from typing import Optional
from pydantic import BaseModel


class WebhookTransaction(BaseModel):
    gateway: str
    transactionDate: str
    accountNumber: str
    subAccount: Optional[str]
    transferType: str
    transferAmount: float
    accumulated: float
    code: Optional[str]
    content: Optional[str]
    referenceCode: Optional[str]
    description: Optional[str] 