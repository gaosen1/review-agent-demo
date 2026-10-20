"""User API handlers."""
import logging

from app.db import get_conn

logger = logging.getLogger(__name__)


def get_user(user_id: int) -> dict | None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
    row = cur.fetchone()
    if row is None:
        return None
    return {"id": row[0], "name": row[1], "email": row[2]}
