from typing import List
from crewai.flow.flow import Flow, start, listen
from tools.news import GetNewsTool, NewsArticle
from pydantic import BaseModel

class State(BaseModel):
    current_articles: List[NewsArticle]

class HumanitysLastHopeFlow(Flow[State]):
    model = "gpt-4.1-nano"

    @start()
    def get_current_news(self):
        print("Fetching current news")
        self.state.current_articles = GetNewsTool().run()

    @listen(get_current_news)
    def discuss(self, previous_result):
        print("Discussing current news")

    


    # recall past history 

    # read today's news

    # discuss

    # take action
    #   - send email
    #   - generate a video
    #   - post on X

    # create a note/report of today (in notion?)

