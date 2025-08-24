from pydantic import BaseModel
from typing import List

class Day(BaseModel):
    date: str # YYYY-MM-DD
    note: str # Note for the day


DAYS_STORE: List[Day] = [] # latest first

def add_day(date: str, note: str) -> None:
    DAYS_STORE.append(Day(date=date, note=note))
    DAYS_STORE.sort(key=lambda x: x.date, reverse=True)

def get_days() -> List[Day]:
    return DAYS_STORE
