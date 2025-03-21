import pytest
from unittest.mock import Mock, patch
from sepay.client import SePayClient, Transaction, BankAccount


@pytest.fixture
def client():
    return SePayClient(api_token="test_token")


@pytest.fixture
def mock_response():
    mock = Mock()
    mock.raise_for_status.return_value = None
    return mock


def test_get_transactions(client, mock_response):
    mock_response.json.return_value = {
        "transactions": [
            {
                "id": "1",
                "transaction_date": "2023-08-09 11:59:47",
                "account_number": "0071000888888",
                "sub_account": "VCB0011ABC001",
                "amount_in": 100000.00,
                "amount_out": 0.00,
                "accumulated": 1777283273.00,
                "code": None,
                "transaction_content": "Test transaction",
                "reference_number": "123456",
                "bank_brand_name": "Vietcombank",
                "bank_account_id": "19"
            }
        ]
    }

    with patch("requests.Session.get", return_value=mock_response):
        transactions = client.get_transactions(account_number="0071000888888")
        assert len(transactions) == 1
        assert isinstance(transactions[0], Transaction)
        assert transactions[0].account_number == "0071000888888"


def test_get_bank_accounts(client, mock_response):
    mock_response.json.return_value = {
        "bankaccounts": [
            {
                "id": "19",
                "account_holder_name": "NGUYEN VAN A",
                "account_number": "0071000888888",
                "accumulated": 1777283273.00,
                "last_transaction": "2023-08-09 11:59:47",
                "label": "Main Account",
                "active": "1",
                "created_at": "2023-02-12 20:05:47",
                "bank_short_name": "Vietcombank",
                "bank_full_name": "Ngân hàng TMCP Ngoại Thương Việt Nam",
                "bank_bin": "970436",
                "bank_code": "VCB"
            }
        ]
    }

    with patch("requests.Session.get", return_value=mock_response):
        accounts = client.get_bank_accounts()
        assert len(accounts) == 1
        assert isinstance(accounts[0], BankAccount)
        assert accounts[0].account_number == "0071000888888"


def test_generate_qr_code(client):
    qr_url = client.generate_qr_code(
        account_number="0071000888888",
        bank_name="Vietcombank",
        amount=100000,
        description="Test payment"
    )
    assert "qr.sepay.vn/img" in qr_url
    assert "acc=0071000888888" in qr_url
    assert "bank=Vietcombank" in qr_url
    assert "amount=100000" in qr_url
    assert "des=Test+payment" in qr_url 