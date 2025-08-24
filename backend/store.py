from pydantic import BaseModel
from typing import List

class Day(BaseModel):
    date: str # YYYY-MM-DD
    summary: str
    video_url: str


DAYS_STORE: List[Day] = [] # latest first

def seed():
    DAYS_STORE.append(Day(date="2025-08-23", summary="This is a test summary", video_url="https://d-id-talks-prod.s3.us-west-2.amazonaws.com/google-oauth2%7C112368331445364818518/tlk_QFf5vn4zJuS5rtIF9aVH4/1755993661383.mp4?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1756080066&Signature=QXRbpRmx5T8%2FIpN1lg3Udr9Cr0c%3D"))
seed()

def add_day(date: str, summary: str, video_url: str) -> None:
    DAYS_STORE.append(Day(date=date, summary=summary, video_url=video_url))
    DAYS_STORE.sort(key=lambda x: x.date, reverse=True)

def get_days() -> List[Day]:
    return DAYS_STORE
