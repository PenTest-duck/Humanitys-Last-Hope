import os
from crewai.tools import BaseTool
from typing import List, Type
from pydantic import BaseModel, Field
import requests
from dotenv import load_dotenv
load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

class NewsArticle(BaseModel):
    title: str
    description: str
    source: str
    url: str
    published_at: str

def get_news_tool() -> List[NewsArticle]:
    response: dict = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI_KEY}").json()
    articles: List[NewsArticle] = []
    for article in response.get("articles", []):
        articles.append(NewsArticle(
            title=article["title"],
            description=article["description"] or article["content"] or "",
            source=article["source"]["name"],
            url=article["url"],
            published_at=article["publishedAt"]
        ))
    return articles

class GetNewsToolInput(BaseModel):
    pass

class GetNewsTool(BaseTool):
    name: str = "Get News"
    description: str = (
        "Get the current top headline news from the web."
    )
    args_schema: Type[BaseModel] = GetNewsToolInput

    def _run(self) -> List[NewsArticle]:
        response: dict = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWSAPI_KEY}").json()
        articles: List[NewsArticle] = []
        for article in response.get("articles", []):
            articles.append(NewsArticle(
                title=article["title"],
                description=article["description"] or article["content"],
                source=article["source"]["name"],
                url=article["url"],
                published_at=article["publishedAt"]
            ))
        return articles

if __name__ == "__main__":
    news_tool = GetNewsTool()
    print(news_tool.run())