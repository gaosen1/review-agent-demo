from decimal import Decimal

from app.pricing import calculate_total


def cart_total(items):
    return sum((calculate_total(Decimal(i["price"]), i["qty"]) for i in items), Decimal(0))
