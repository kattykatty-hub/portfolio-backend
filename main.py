from database import conn, cursor
from datetime import datetime

@app.post("/contact")
def submit_contact(data: ContactMessage):
    cursor.execute(
        "INSERT INTO contacts (name, email, message, created_at) VALUES (?, ?, ?, ?)",
        (data.name, data.email, data.message, datetime.utcnow().isoformat())
    )
    conn.commit()

    return {"status": "stored"}
