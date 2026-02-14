from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "AI Tutor Backend Running 🚀"}

@app.get("/get-task")
def get_task():
    return {
        "task_id": 1,
        "prompt": "Introduce yourself in English."
    }

@app.post("/submit-score")
def submit_score(fluency: int, grammar: int, accuracy: int):
    status = "Practice Required"
    if fluency >= 90 and grammar >= 90 and accuracy >= 90:
        status = "Level Up 🎉"

    return {
        "fluency": fluency,
        "grammar": grammar,
        "accuracy": accuracy,
        "status": status
    }
