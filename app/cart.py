from decimal import Decimal

from app.pricing import calc


def cart_total(items):
    return sum((calc(Decimal(i["price"]), i["qty"]) for i in items), Decimal(0))
