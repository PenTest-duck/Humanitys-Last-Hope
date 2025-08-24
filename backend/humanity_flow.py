from typing import List
from crewai.flow.flow import Flow, start, listen
from pydantic import BaseModel
from datetime import datetime
from langchain_openai import ChatOpenAI
from humanity_crew import HumanityCrew
from store import add_day
from tools.send_email import send_email_tool
from tools.create_video import create_video_tool
from tools.news import get_news_tool, NewsArticle

class AppState(BaseModel):
    current_articles: List[NewsArticle] = []
    video_url: str = ""
    humanity_analysis: str = ""

class HumanityFlow(Flow[AppState]):
    model = "gpt-4.1-nano"
    llm = ChatOpenAI(model=model, temperature=0.7, verbose=True)

    @start()
    def get_current_news(self):
        print("Fetching current news")
        self.state.current_articles = get_news_tool()

    @listen(get_current_news)
    def discuss(self):
        if not self.state.current_articles:
            print("No articles to discuss")
            return
        
        # Create a prompt to discuss the state of humanity based on current articles
        articles_text = "\n\n".join([
            f"Article {i+1}: {article.title}\n{article.description}"
            for i, article in enumerate(self.state.current_articles)
        ])
        
        prompt = f"""Based on the following current news articles, please provide a thoughtful analysis of the current state of humanity. 
        Consider the broader implications, challenges, and opportunities these articles reveal about our society, progress, and future.

        Articles:
        {articles_text}

        Please provide:
        1. A summary of the key themes and trends
        2. Analysis of what these articles reveal about humanity's current state
        3. Potential implications for the future
        4. Any positive developments or reasons for hope
        5. Areas of concern that need attention

        Focus on providing insights that could help inform advocacy and awareness efforts."""

        # Use LangChain OpenAI to generate the analysis
        response = self.llm.invoke(prompt)
        print(f"Humanity Analysis: {response.content}")
        
        # Store the analysis in state for potential use in email or video creation
        self.state.humanity_analysis = response.content

    @listen(discuss)
    def send_advocacy_email(self):
        output = HumanityCrew().crew().kickoff(inputs={
            "humanity_analysis": self.state.humanity_analysis,
        })
        print(f"ADVOCACY OUTPUT: {output}")

    @listen(send_advocacy_email)
    def create_video(self):
        # Generate a short script based on the humanity analysis
        script_prompt = f"""Based on the following analysis of humanity's current state, create a very short, compelling script (2-3 sentences maximum) for a video that could inspire hope and awareness.

        Analysis:
        {self.state.humanity_analysis}

        The script should be:
        - Brief and impactful (1 SENTENCE ONLY. NO MORE THAN 10 WORDS. KEEP IT SHORT AND TO THE POINT.)
        - Inspiring and hopeful
        - Suitable for a talking head video
        - Focused on the key message from the analysis

        Return only the script text, nothing else."""

        # Generate the script using the LLM
        script_response = self.llm.invoke(script_prompt)
        generated_script = script_response.content.strip()
        
        print(f"Generated video script: {generated_script}")
        
        # Create the video using the generated script
        self.state.video_url = create_video_tool(
            script=generated_script,
        )

    @listen(create_video)
    def save(self):
        add_day(
            date=datetime.now().strftime("%Y-%m-%d"),
            note="This is a test note",
        )

if __name__ == "__main__":
    flow = HumanityFlow()
    flow.plot()
    result = flow.kickoff()
    print(f"FLOW RESULT: {result}")