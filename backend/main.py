from fastapi import FastAPI
from pydantic import BaseModel
import json
import random

app = FastAPI()

# Load datasets
with open("datasets/grammar_dataset.json", "r") as f:
    grammar_data = json.load(f)

with open("datasets/vocabulary_dataset.json", "r") as f:
    vocabulary_data = json.load(f)


class UserAnswer(BaseModel):
    question: str
    answer: str


@app.get("/")
def home():
    return {"message": "English AI Tutor Backend Running"}


@app.get("/get-grammar-question")
def get_grammar_question():
    return random.choice(grammar_data)


@app.get("/get-vocabulary-question")
def get_vocab_question():
    return random.choice(vocabulary_data)


@app.post("/check-answer")
def check_answer(user: UserAnswer):
    for item in grammar_data + vocabulary_data:
        if item["question"] == user.question:
            correct_answer = item["answer"]
            if user.answer.lower() == correct_answer.lower():
                return {"result": "Correct ✅"}
            else:
                return {
                    "result": "Incorrect ❌",
                    "correct_answer": correct_answer
                }

    return {"result": "Question not found"}
