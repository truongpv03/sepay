# SePay SDK

Python SDK for SePay payment integration.

## Installation

```bash
poetry add sepay-sdk
```

## Usage

```python
from sepay import SePayClient

# Initialize client
client = SePayClient(api_token="your_api_token")

# Get transactions
transactions = client.get_transactions(
    account_number="0071000888888",
    limit=20
)

# Get bank accounts
bank_accounts = client.get_bank_accounts()

# Generate QR code
qr_code_url = client.generate_qr_code(
    account_number="0071000888888",
    bank_name="Vietcombank",
    amount=100000,
    description="Payment for Order #123"
)

# Handle webhooks
from sepay.webhooks import WebhookHandler

def handle_transaction(transaction):
    print(f"Received transaction: {transaction}")

handler = WebhookHandler(secret="your_webhook_secret")
handler.on_transaction(handle_transaction)
```

## Features

- Transaction management
- Bank account management
- QR code generation
- Webhook handling

## Development

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Format code
poetry run black .
poetry run isort .
```

## License

MIT 