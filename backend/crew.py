from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class HumanitysLastHopeCrew(CrewBase):
    @agent
    def agent(self) -> Agent:
        pass

    @task
    def some_task(self) -> Task:
        return Task(
            config=self.tasks_config["some_task"],
        )