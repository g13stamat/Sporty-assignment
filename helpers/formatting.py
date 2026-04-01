# helpers/formatting.py

def extract_text(raw: str) -> str:
    """
    Ensures the text is clean and stripped of whitespace.
    """
    if raw is None:
        return ""
    return raw.strip()


def strip_currency(value: str) -> str:
    """
    Removes currency symbols like € and commas.
    """
    if value is None:
        return ""
    return (
        value.replace("€", "")
             .replace(",", "")
             .strip()
    )


def to_float(value: str) -> float:
    if value is None:
        return 0.0

    value = value.strip()
    if value == "":
        return 0.0

    return float(value)



def round2(value: float) -> float:
    """
    Rounds a float to 2 decimal places.
    """
    return round(value, 2)


def calculate_payout(odds: float, stake: float) -> float:
    """
    Standard sportsbook payout formula:
    payout = odds * stake, rounded to 2 decimals.
    """
    return round2(odds * stake)