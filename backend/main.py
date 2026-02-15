from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os
from datetime import datetime

app = FastAPI()

DATA_PATH = "datasets"
USERS_FILE = os.path.join(DATA_PATH, "users.csv")


# ---------- Models ----------

class RegisterRequest(BaseModel):
    name: str
    branch: str
    year_of_study: int


class LoginRequest(BaseModel):
    user_id: str


# ---------- Routes ----------

@app.get("/")
def home():
    return {"message": "AI Tutor Backend Running"}


@app.post("/register")
def register_user(request: RegisterRequest):

    df = pd.read_csv(USERS_FILE)

    # Generate new user ID
    new_id = f"U{len(df)+1:03}"

    new_user = {
        "user_id": new_id,
        "branch": request.branch,
        "year_of_study": request.year_of_study,
        "course": "English Speaking",
        "current_level": "Beginner",
        "created_at": datetime.now()
    }

    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
    df.to_csv(USERS_FILE, index=False)

    return {
        "message": "User registered successfully",
        "user_id": new_id,
        "current_level": "Beginner"
    }


@app.post("/login")
def login_user(request: LoginRequest):

    df = pd.read_csv(USERS_FILE)

    user = df[df["user_id"] == request.user_id]

    if user.empty:
        return {"error": "User not found"}

    return {
        "message": "Login successful",
        "user_id": request.user_id,
        "current_level": user.iloc[0]["current_level"]
    }
