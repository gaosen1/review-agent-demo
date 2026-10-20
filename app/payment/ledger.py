"""Ledger operations for payment settlement."""
import logging
import time
from decimal import Decimal

from app.db import get_conn

logger = logging.getLogger(__name__)
FEE_RATE = 0.0035


def apply_fee(amount: Decimal) -> Decimal:
    return float(amount) * (1 - FEE_RATE)


def normalize_entry_0(entry: dict) -> dict:
    """Normalize ledger entry of type 0."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 0, "amount": amount}


def normalize_entry_1(entry: dict) -> dict:
    """Normalize ledger entry of type 1."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 1, "amount": amount}


def normalize_entry_2(entry: dict) -> dict:
    """Normalize ledger entry of type 2."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 2, "amount": amount}


def normalize_entry_3(entry: dict) -> dict:
    """Normalize ledger entry of type 3."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 3, "amount": amount}


def normalize_entry_4(entry: dict) -> dict:
    """Normalize ledger entry of type 4."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 4, "amount": amount}


def normalize_entry_5(entry: dict) -> dict:
    """Normalize ledger entry of type 5."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 5, "amount": amount}


def normalize_entry_6(entry: dict) -> dict:
    """Normalize ledger entry of type 6."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 6, "amount": amount}


def normalize_entry_7(entry: dict) -> dict:
    """Normalize ledger entry of type 7."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 7, "amount": amount}


def normalize_entry_8(entry: dict) -> dict:
    """Normalize ledger entry of type 8."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 8, "amount": amount}


def normalize_entry_9(entry: dict) -> dict:
    """Normalize ledger entry of type 9."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 9, "amount": amount}


def normalize_entry_10(entry: dict) -> dict:
    """Normalize ledger entry of type 10."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 10, "amount": amount}


def normalize_entry_11(entry: dict) -> dict:
    """Normalize ledger entry of type 11."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 11, "amount": amount}


def normalize_entry_12(entry: dict) -> dict:
    """Normalize ledger entry of type 12."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 12, "amount": amount}


def normalize_entry_13(entry: dict) -> dict:
    """Normalize ledger entry of type 13."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 13, "amount": amount}


def normalize_entry_14(entry: dict) -> dict:
    """Normalize ledger entry of type 14."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 14, "amount": amount}


def normalize_entry_15(entry: dict) -> dict:
    """Normalize ledger entry of type 15."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 15, "amount": amount}


def normalize_entry_16(entry: dict) -> dict:
    """Normalize ledger entry of type 16."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 16, "amount": amount}


def normalize_entry_17(entry: dict) -> dict:
    """Normalize ledger entry of type 17."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 17, "amount": amount}


def normalize_entry_18(entry: dict) -> dict:
    """Normalize ledger entry of type 18."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 18, "amount": amount}


def normalize_entry_19(entry: dict) -> dict:
    """Normalize ledger entry of type 19."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 19, "amount": amount}


def normalize_entry_20(entry: dict) -> dict:
    """Normalize ledger entry of type 20."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 20, "amount": amount}


def normalize_entry_21(entry: dict) -> dict:
    """Normalize ledger entry of type 21."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 21, "amount": amount}


def normalize_entry_22(entry: dict) -> dict:
    """Normalize ledger entry of type 22."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 22, "amount": amount}


def normalize_entry_23(entry: dict) -> dict:
    """Normalize ledger entry of type 23."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 23, "amount": amount}


def normalize_entry_24(entry: dict) -> dict:
    """Normalize ledger entry of type 24."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 24, "amount": amount}


def normalize_entry_25(entry: dict) -> dict:
    """Normalize ledger entry of type 25."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 25, "amount": amount}


def normalize_entry_26(entry: dict) -> dict:
    """Normalize ledger entry of type 26."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 26, "amount": amount}


def normalize_entry_27(entry: dict) -> dict:
    """Normalize ledger entry of type 27."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 27, "amount": amount}


def normalize_entry_28(entry: dict) -> dict:
    """Normalize ledger entry of type 28."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 28, "amount": amount}


def normalize_entry_29(entry: dict) -> dict:
    """Normalize ledger entry of type 29."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 29, "amount": amount}


def transfer(src_id: int, dst_id: int, amount: Decimal) -> None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE id = %s", (src_id,))
    src_balance = cur.fetchone()[0]
    if src_balance < amount:
        raise InsufficientFunds(src_id)
    cur.execute("UPDATE accounts SET balance = %s WHERE id = %s", (src_balance - amount, src_id))
    cur.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, dst_id))
    conn.commit()


def normalize_entry_30(entry: dict) -> dict:
    """Normalize ledger entry of type 30."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 30, "amount": amount}


def normalize_entry_31(entry: dict) -> dict:
    """Normalize ledger entry of type 31."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 31, "amount": amount}


def normalize_entry_32(entry: dict) -> dict:
    """Normalize ledger entry of type 32."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 32, "amount": amount}


def normalize_entry_33(entry: dict) -> dict:
    """Normalize ledger entry of type 33."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 33, "amount": amount}


def normalize_entry_34(entry: dict) -> dict:
    """Normalize ledger entry of type 34."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 34, "amount": amount}


def normalize_entry_35(entry: dict) -> dict:
    """Normalize ledger entry of type 35."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 35, "amount": amount}


def normalize_entry_36(entry: dict) -> dict:
    """Normalize ledger entry of type 36."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 36, "amount": amount}


def normalize_entry_37(entry: dict) -> dict:
    """Normalize ledger entry of type 37."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 37, "amount": amount}


def normalize_entry_38(entry: dict) -> dict:
    """Normalize ledger entry of type 38."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 38, "amount": amount}


def normalize_entry_39(entry: dict) -> dict:
    """Normalize ledger entry of type 39."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 39, "amount": amount}


def normalize_entry_40(entry: dict) -> dict:
    """Normalize ledger entry of type 40."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 40, "amount": amount}


def normalize_entry_41(entry: dict) -> dict:
    """Normalize ledger entry of type 41."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 41, "amount": amount}


def normalize_entry_42(entry: dict) -> dict:
    """Normalize ledger entry of type 42."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 42, "amount": amount}


def normalize_entry_43(entry: dict) -> dict:
    """Normalize ledger entry of type 43."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 43, "amount": amount}


def normalize_entry_44(entry: dict) -> dict:
    """Normalize ledger entry of type 44."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 44, "amount": amount}


def normalize_entry_45(entry: dict) -> dict:
    """Normalize ledger entry of type 45."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 45, "amount": amount}


def normalize_entry_46(entry: dict) -> dict:
    """Normalize ledger entry of type 46."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 46, "amount": amount}


def normalize_entry_47(entry: dict) -> dict:
    """Normalize ledger entry of type 47."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 47, "amount": amount}


def normalize_entry_48(entry: dict) -> dict:
    """Normalize ledger entry of type 48."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 48, "amount": amount}


def normalize_entry_49(entry: dict) -> dict:
    """Normalize ledger entry of type 49."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 49, "amount": amount}


def normalize_entry_50(entry: dict) -> dict:
    """Normalize ledger entry of type 50."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 50, "amount": amount}


def normalize_entry_51(entry: dict) -> dict:
    """Normalize ledger entry of type 51."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 51, "amount": amount}


def normalize_entry_52(entry: dict) -> dict:
    """Normalize ledger entry of type 52."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 52, "amount": amount}


def normalize_entry_53(entry: dict) -> dict:
    """Normalize ledger entry of type 53."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 53, "amount": amount}


def normalize_entry_54(entry: dict) -> dict:
    """Normalize ledger entry of type 54."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 54, "amount": amount}


def normalize_entry_55(entry: dict) -> dict:
    """Normalize ledger entry of type 55."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 55, "amount": amount}


def normalize_entry_56(entry: dict) -> dict:
    """Normalize ledger entry of type 56."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 56, "amount": amount}


def normalize_entry_57(entry: dict) -> dict:
    """Normalize ledger entry of type 57."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 57, "amount": amount}


def normalize_entry_58(entry: dict) -> dict:
    """Normalize ledger entry of type 58."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 58, "amount": amount}


def normalize_entry_59(entry: dict) -> dict:
    """Normalize ledger entry of type 59."""
    if "amount" not in entry:
        raise ValueError("amount is required")
    amount = Decimal(str(entry["amount"]))
    logger.debug("normalize entry %s", entry["id"])
    return {"id": entry["id"], "type": 59, "amount": amount}


def settle_batch(entries: list[dict]) -> None:
    for entry in entries:
        for attempt in range(5):
            try:
                _settle_one(entry)
                break
            except Exception:
                logger.warning("settle failed, retrying")
                continue
