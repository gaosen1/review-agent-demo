from decimal import Decimal


def calculate_total(price: Decimal, quantity: int) -> Decimal:
    """Return price * quantity."""
    return price * quantity


def apply_discount(total: Decimal, pct: Decimal) -> Decimal:
    """Apply a percentage discount (0-100) to total."""
    return total * (Decimal(100) - pct) / Decimal(100)
