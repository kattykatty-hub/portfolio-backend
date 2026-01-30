import sqlite3

conn = sqlite3.connect("contacts.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT,
  message TEXT,
  created_at TEXT
)
""")

conn.commit()

@app.get("/")
def health():
    return {"status": "ok"}



