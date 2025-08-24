import requests
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from crewai.tools import BaseTool
from typing import List, Type
from time import sleep

load_dotenv()
D_ID_API_KEY = os.getenv("D_ID_API_KEY")
D_ID_URL = "https://api.d-id.com/talks"

def create_video_tool(script: str) -> str:
    payload = {
        "source_url": "https://d-id-public-bucket.s3.us-west-2.amazonaws.com/alice.jpg",
        "script": {
            "type": "text",
            "subtitles": "false",
            "provider": {
                "type": "microsoft",
                "voice_id": "en-US-JennyNeural"
            },
            "input": script,
            "ssml": "false"
        },
        "config": { "fluent": "false" }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Basic {D_ID_API_KEY}"
    }
    response = requests.post(D_ID_URL, json=payload, headers=headers)
    print(response.json())
    talk_id = response.json()["id"]
    print(f"Video created. Talk ID: {talk_id}")
    
    while True:
        sleep(1)
        response = requests.get(f"{D_ID_URL}/{talk_id}", headers=headers)
        print(response.json())
        status = response.json()["status"]
        print(f"Checking status...")
        if status == "done":
            url = response.json()["result_url"]
            print(f"Video available at {url}")
            return url

class CreateVideoToolInput(BaseModel):
    script: str

class CreateVideoTool(BaseTool):
    name: str = "Create Video"
    description: str = (
        "Create a video from a script. This creates a talking head video of a person speaking the script."
    )
    args_schema: Type[BaseModel] = CreateVideoToolInput

    def _run(self) -> str:
        payload = {
            "source_url": "https://d-id-public-bucket.s3.us-west-2.amazonaws.com/alice.jpg",
            "script": {
                "type": "text",
                "subtitles": "true",
                "provider": {
                    "type": "microsoft",
                    "voice_id": "en-US-JennyNeural"
                },
                "input": self.input.script,
                "ssml": "false"
            },
            "config": { "fluent": "false" }
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {D_ID_API_KEY}"
        }
        response = requests.post(D_ID_URL, json=payload, headers=headers)
        talk_id = response.json()["id"]
        print(f"Video successfully created. Talk ID: {talk_id}")
        return "Video successfully created."

if __name__ == "__main__":
    print(create_video_tool("Hello world"))