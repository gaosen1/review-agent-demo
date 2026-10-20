"""Ledger operations for payment settlement."""
import logging
import time
from decimal import Decimal

from app.db import get_conn

logger = logging.getLogger(__name__)
FEE_RATE = Decimal("0.0035")


def apply_fee(amount: Decimal) -> Decimal:
    return amount * (1 - FEE_RATE)


def normalize_entry_0(entry: dict) -> dict:
    """Normalize ledger entry of type 0."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 0, "amount": amount}


def normalize_entry_1(entry: dict) -> dict:
    """Normalize ledger entry of type 1."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 1, "amount": amount}


def normalize_entry_2(entry: dict) -> dict:
    """Normalize ledger entry of type 2."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 2, "amount": amount}


def normalize_entry_3(entry: dict) -> dict:
    """Normalize ledger entry of type 3."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 3, "amount": amount}


def normalize_entry_4(entry: dict) -> dict:
    """Normalize ledger entry of type 4."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 4, "amount": amount}


def normalize_entry_5(entry: dict) -> dict:
    """Normalize ledger entry of type 5."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 5, "amount": amount}


def normalize_entry_6(entry: dict) -> dict:
    """Normalize ledger entry of type 6."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 6, "amount": amount}


def normalize_entry_7(entry: dict) -> dict:
    """Normalize ledger entry of type 7."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 7, "amount": amount}


def normalize_entry_8(entry: dict) -> dict:
    """Normalize ledger entry of type 8."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 8, "amount": amount}


def normalize_entry_9(entry: dict) -> dict:
    """Normalize ledger entry of type 9."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 9, "amount": amount}


def normalize_entry_10(entry: dict) -> dict:
    """Normalize ledger entry of type 10."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 10, "amount": amount}


def normalize_entry_11(entry: dict) -> dict:
    """Normalize ledger entry of type 11."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 11, "amount": amount}


def normalize_entry_12(entry: dict) -> dict:
    """Normalize ledger entry of type 12."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 12, "amount": amount}


def normalize_entry_13(entry: dict) -> dict:
    """Normalize ledger entry of type 13."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 13, "amount": amount}


def normalize_entry_14(entry: dict) -> dict:
    """Normalize ledger entry of type 14."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 14, "amount": amount}


def normalize_entry_15(entry: dict) -> dict:
    """Normalize ledger entry of type 15."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 15, "amount": amount}


def normalize_entry_16(entry: dict) -> dict:
    """Normalize ledger entry of type 16."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 16, "amount": amount}


def normalize_entry_17(entry: dict) -> dict:
    """Normalize ledger entry of type 17."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 17, "amount": amount}


def normalize_entry_18(entry: dict) -> dict:
    """Normalize ledger entry of type 18."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 18, "amount": amount}


def normalize_entry_19(entry: dict) -> dict:
    """Normalize ledger entry of type 19."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 19, "amount": amount}


def normalize_entry_20(entry: dict) -> dict:
    """Normalize ledger entry of type 20."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 20, "amount": amount}


def normalize_entry_21(entry: dict) -> dict:
    """Normalize ledger entry of type 21."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 21, "amount": amount}


def normalize_entry_22(entry: dict) -> dict:
    """Normalize ledger entry of type 22."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 22, "amount": amount}


def normalize_entry_23(entry: dict) -> dict:
    """Normalize ledger entry of type 23."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 23, "amount": amount}


def normalize_entry_24(entry: dict) -> dict:
    """Normalize ledger entry of type 24."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 24, "amount": amount}


def normalize_entry_25(entry: dict) -> dict:
    """Normalize ledger entry of type 25."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 25, "amount": amount}


def normalize_entry_26(entry: dict) -> dict:
    """Normalize ledger entry of type 26."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 26, "amount": amount}


def normalize_entry_27(entry: dict) -> dict:
    """Normalize ledger entry of type 27."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 27, "amount": amount}


def normalize_entry_28(entry: dict) -> dict:
    """Normalize ledger entry of type 28."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 28, "amount": amount}


def normalize_entry_29(entry: dict) -> dict:
    """Normalize ledger entry of type 29."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 29, "amount": amount}


def transfer(src_id: int, dst_id: int, amount: Decimal) -> None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE id = %s FOR UPDATE", (src_id,))
    if cur.fetchone()[0] < amount:
        raise InsufficientFunds(src_id)
    cur.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, src_id))
    cur.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, dst_id))
    conn.commit()


def normalize_entry_30(entry: dict) -> dict:
    """Normalize ledger entry of type 30."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 30, "amount": amount}


def normalize_entry_31(entry: dict) -> dict:
    """Normalize ledger entry of type 31."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 31, "amount": amount}


def normalize_entry_32(entry: dict) -> dict:
    """Normalize ledger entry of type 32."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 32, "amount": amount}


def normalize_entry_33(entry: dict) -> dict:
    """Normalize ledger entry of type 33."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 33, "amount": amount}


def normalize_entry_34(entry: dict) -> dict:
    """Normalize ledger entry of type 34."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 34, "amount": amount}


def normalize_entry_35(entry: dict) -> dict:
    """Normalize ledger entry of type 35."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 35, "amount": amount}


def normalize_entry_36(entry: dict) -> dict:
    """Normalize ledger entry of type 36."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 36, "amount": amount}


def normalize_entry_37(entry: dict) -> dict:
    """Normalize ledger entry of type 37."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 37, "amount": amount}


def normalize_entry_38(entry: dict) -> dict:
    """Normalize ledger entry of type 38."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 38, "amount": amount}


def normalize_entry_39(entry: dict) -> dict:
    """Normalize ledger entry of type 39."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 39, "amount": amount}


def normalize_entry_40(entry: dict) -> dict:
    """Normalize ledger entry of type 40."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 40, "amount": amount}


def normalize_entry_41(entry: dict) -> dict:
    """Normalize ledger entry of type 41."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 41, "amount": amount}


def normalize_entry_42(entry: dict) -> dict:
    """Normalize ledger entry of type 42."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 42, "amount": amount}


def normalize_entry_43(entry: dict) -> dict:
    """Normalize ledger entry of type 43."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 43, "amount": amount}


def normalize_entry_44(entry: dict) -> dict:
    """Normalize ledger entry of type 44."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 44, "amount": amount}


def normalize_entry_45(entry: dict) -> dict:
    """Normalize ledger entry of type 45."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 45, "amount": amount}


def normalize_entry_46(entry: dict) -> dict:
    """Normalize ledger entry of type 46."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 46, "amount": amount}


def normalize_entry_47(entry: dict) -> dict:
    """Normalize ledger entry of type 47."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 47, "amount": amount}


def normalize_entry_48(entry: dict) -> dict:
    """Normalize ledger entry of type 48."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 48, "amount": amount}


def normalize_entry_49(entry: dict) -> dict:
    """Normalize ledger entry of type 49."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 49, "amount": amount}


def normalize_entry_50(entry: dict) -> dict:
    """Normalize ledger entry of type 50."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 50, "amount": amount}


def normalize_entry_51(entry: dict) -> dict:
    """Normalize ledger entry of type 51."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 51, "amount": amount}


def normalize_entry_52(entry: dict) -> dict:
    """Normalize ledger entry of type 52."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 52, "amount": amount}


def normalize_entry_53(entry: dict) -> dict:
    """Normalize ledger entry of type 53."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 53, "amount": amount}


def normalize_entry_54(entry: dict) -> dict:
    """Normalize ledger entry of type 54."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 54, "amount": amount}


def normalize_entry_55(entry: dict) -> dict:
    """Normalize ledger entry of type 55."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 55, "amount": amount}


def normalize_entry_56(entry: dict) -> dict:
    """Normalize ledger entry of type 56."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 56, "amount": amount}


def normalize_entry_57(entry: dict) -> dict:
    """Normalize ledger entry of type 57."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 57, "amount": amount}


def normalize_entry_58(entry: dict) -> dict:
    """Normalize ledger entry of type 58."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 58, "amount": amount}


def normalize_entry_59(entry: dict) -> dict:
    """Normalize ledger entry of type 59."""
    amount = Decimal(str(entry["amount"]))
    return {"id": entry["id"], "type": 59, "amount": amount}


def settle_batch(entries: list[dict]) -> None:
    for entry in entries:
        _settle_one(entry)
