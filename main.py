from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from datetime import datetime
from database import conn, cursor
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for portfolio; restrict later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
