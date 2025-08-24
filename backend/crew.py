from typing import List
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

knowledge_source = StringKnowledgeSource(content="""
Here are core, timeless values of humanity.
""")

@CrewBase
class HumanitysLastHopeCrew(CrewBase):
    agents: List[BaseAgent] = []
    tasks: List[Task] = []

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @before_kickoff
    def before(self):
        pass

    @after_kickoff
    def after(self):
        pass

    @agent
    def agent(self) -> Agent:
        return Agent(
            role="",
            goal="",
            backstory="",
            verbose=True,
            tools=[],
            allow_delegation=False,
        )

    @task
    def some_task(self) -> Task:
        return Task(
            config=self.tasks_config["some_task"],
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
    
def kickoff():
    crew = HumanitysLastHopeCrew().crew()
    crew.kickoff(inputs={})

if __name__ == "__main__":
    kickoff()