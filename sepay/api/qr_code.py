from typing import Optional


class QRCodeAPI:
    @staticmethod
    def generate_qr_code(
        account_number: str,
        bank_name: str,
        amount: Optional[float] = None,
        description: Optional[str] = None
    ) -> str:
        """Generate QR code URL for payment."""
        params = {
            "acc": account_number,
            "bank": bank_name,
            "amount": amount,
            "des": description
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        return f"https://qr.sepay.vn/img?{'&'.join(f'{k}={v}' for k, v in params.items())}"