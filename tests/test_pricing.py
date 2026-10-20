from decimal import Decimal

from app.pricing import apply_discount, calculate_total


def test_calculate_total():
    assert calculate_total(Decimal("2.50"), 4) == Decimal("10.00")


def test_apply_discount():
    assert apply_discount(Decimal("200"), Decimal("25")) == Decimal("150")
