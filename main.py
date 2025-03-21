from sepay import SePayClient, WebhookHandler

# Khởi tạo client
client = SePayClient(api_token="your_api_token")

# Sử dụng các API
transactions = client.get_transactions(account_number="0071000888888")
bank_accounts = client.get_bank_accounts()
qr_url = client.generate_qr_code(account_number="0071000888888", bank_name="Vietcombank")

# Xử lý webhooks
handler = WebhookHandler(secret="your_webhook_secret")
handler.on_transaction(lambda t: print(f"Received transaction: {t}"))