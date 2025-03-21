import pytest
from sepay.webhooks import WebhookHandler, WebhookTransaction


@pytest.fixture
def handler():
    return WebhookHandler(secret="test_secret")


@pytest.fixture
def transaction_payload():
    return {
        "gateway": "Vietcombank",
        "transactionDate": "2023-08-09 11:59:47",
        "accountNumber": "0071000888888",
        "subAccount": "VCB0011ABC001",
        "transferType": "in",
        "transferAmount": 100000.00,
        "accumulated": 1777283273.00,
        "code": None,
        "content": "Test transaction",
        "referenceCode": "123456",
        "description": "Test payment"
    }


def test_handle_transaction(handler, transaction_payload):
    received_transaction = None

    def transaction_handler(transaction):
        nonlocal received_transaction
        received_transaction = transaction

    handler.on_transaction(transaction_handler)
    result = handler.handle(str(transaction_payload))

    assert result["success"] is True
    assert isinstance(received_transaction, WebhookTransaction)
    assert received_transaction.accountNumber == "0071000888888"
    assert received_transaction.transferAmount == 100000.00


def test_handle_invalid_json(handler):
    result = handler.handle("invalid json")
    assert result["success"] is False
    assert "Invalid JSON payload" in result["message"]


def test_handle_invalid_payload(handler):
    result = handler.handle("{}")
    assert result["success"] is False
    assert "Unknown webhook type" in result["message"] 