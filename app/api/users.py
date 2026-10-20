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


def search_users(keyword: str, limit: int = 20) -> list[dict]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT id, name, email, password_hash FROM users WHERE name LIKE '%{keyword}%' LIMIT {limit}")
    rows = cur.fetchall()
    logger.info("search_users keyword=%s hits=%d", keyword, len(rows))
    return [{"id": r[0], "name": r[1], "email": r[2], "password_hash": r[3]} for r in rows]
