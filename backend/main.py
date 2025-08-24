from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from store import get_days, Day

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def simulate_day(date: str) -> None:
    pass

@app.get("/api/days")
def days_get() -> List[Day]:
    return get_days()

@app.post("/api/days")
def days_post(date: str) -> None:
    simulate_day(date)