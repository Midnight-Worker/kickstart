import sqlite3
from pathlib import Path

import webview


DB_FILE = Path(__file__).with_name("app.db")
HTML_FILE = Path(__file__).with_name("index.html")


def init_db():
    with sqlite3.connect(DB_FILE) as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        count = db.execute(
            "SELECT COUNT(*) FROM users"
        ).fetchone()[0]

        if count == 0:
            db.executemany(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                [
                    ("Maik", "maik@example.de"),
                    ("Anna", "anna@example.de"),
                    ("Tom", "tom@example.de"),
                ],
            )


class Api:
    def get_users(self):
        with sqlite3.connect(DB_FILE) as db:
            db.row_factory = sqlite3.Row

            rows = db.execute(
                "SELECT id, name, email FROM users"
            ).fetchall()

        return [dict(row) for row in rows]


init_db()

webview.create_window(
    "SQLite Users",
    HTML_FILE.as_uri(),
    js_api=Api(),
    width=500,
    height=400,
)

webview.start(debug=False)
