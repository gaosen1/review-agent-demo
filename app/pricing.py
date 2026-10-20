from decimal import Decimal


def calc(p, q):
    return p * q


def apply_discount(total, pct):
    return total * (Decimal(100) - pct) / Decimal(100)
