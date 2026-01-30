from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from datetime import datetime
from database import conn, cursor

app = FastAPI(title="Portfolio Contact API")

# -------------------
# Data model
# -------------------
class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    message: str

# -------------------
# Health check
# -------------------
@app.get("/")
def health():
    return {"status": "ok"}

# -------------------
# Contact endpoint
# -------------------
@app.post("/contact")
def submit_contact(data: ContactMessage):
    cursor.execute(
        """
        INSERT INTO contacts (name, email, message, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (data.name, data.email, data.message, datetime.utcnow().isoformat())
    )
    conn.commit()

    return {"status": "stored"}
