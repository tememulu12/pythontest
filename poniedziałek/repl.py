from _decimal import Decimal


def clean_decimal(text: str | None) -> Decimal | None:
    if text is None: return None
    return Decimal(
        text.replace("$", '').replace(",", "")
    )

