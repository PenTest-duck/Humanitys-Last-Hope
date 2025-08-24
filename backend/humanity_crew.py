from typing import List
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from pydantic import BaseModel
from tools.send_email import SendEmailTool
from tools.news import GetNewsTool
from knowledge import knowledge_source
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
load_dotenv()

class AdvocacyOutput(BaseModel):
    resulting_summary: str


@CrewBase
class HumanityCrew:
    """Humanity crew"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # @agent
    # def analysis_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["analysis_agent"],
    #         verbose=True,
    #         tools=[GetNewsTool()],
    #         allow_delegation=True,
    #     )

    # @task
    # def analyse_state_of_humanity(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["analyse_state_of_humanity"],
    #         output_pydantic=AnalysisOutput,
    #     )
    
    @agent
    def advocacy_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["advocacy_agent"],
            verbose=True,
            tools=[
                SendEmailTool(),
                SerperDevTool(),
            ],
            allow_delegation=False,
        )

    @task
    def advocate_for_action(self) -> Task:
        return Task(
            config=self.tasks_config["advocate_for_action"],
            output_pydantic=AdvocacyOutput,
        )
        
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
        )

if __name__ == "__main__":
    output = HumanityCrew().crew().kickoff(inputs={})
    print(output)
