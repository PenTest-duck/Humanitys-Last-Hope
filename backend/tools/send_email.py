import os
from crewai.tools import BaseTool
from typing import List, Type
from pydantic import BaseModel, Field
import requests
import resend
from dotenv import load_dotenv
load_dotenv()

RESEND_KEY = os.getenv("RESEND_KEY")
if RESEND_KEY:
    resend.api_key = RESEND_KEY

def send_email_tool(to: List[str], subject: str, html: str) -> None:
    params: resend.Emails.SendParams = {
        "from": "Guardians of Humanity <onboarding@resend.dev>",
        "to": ["delivered@resend.dev"], # to,
        "subject": subject,
        "html": html,
    }
    email = resend.Emails.send(params)
    print(f"Sent email to {to} with subject {subject}")

class SendEmailToolInput(BaseModel):
    to: str
    subject: str
    html: str

class SendEmailTool(BaseTool):
    name: str = "Send Email"
    description: str = (
        "Send an email to a recipient."
    )
    args_schema: Type[BaseModel] = SendEmailToolInput

    def _run(self) -> None:
        params: resend.Emails.SendParams = {
            "from": "Guardian of Humanity <onboarding@resend.dev>",
            "to": ["delivered@resend.dev"], # [self.input.to],
            "subject": self.input.subject,
            "html": self.input.html,
        }
        email = resend.Emails.send(params)
        print(f"Sent email to {self.input.to} with subject {self.input.subject}")

if __name__ == "__main__":
    params: resend.Emails.SendParams = {
        "from": "Guardian of Humanity <onboarding@resend.dev>",
        "to": ["delivered@resend.dev"], # [self.input.to],
        "subject": "Test Email",
        "html": "This is a test email",
    }
    print(params)
    email: resend.Email = resend.Emails.send(params)
    # email = resend.Emails.send(params)