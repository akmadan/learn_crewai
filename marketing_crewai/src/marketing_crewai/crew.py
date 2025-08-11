from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool

@CrewBase
class MarketingCrew():
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_agent'],
            tools=[SerperDevTool()],
            verbose=True
        )
    
    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'],
            verbose=True
        )

    @agent
    def reviewer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['reviewer_agent'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agents=[self.research_agent],
            tools=[SerperDevTool()],
            verbose=True
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
            agents=[self.writer_agent],
            output_file='output.md',
            verbose=True
        )

    @task
    def reviewing_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewing_task'],
            agents=[self.reviewer_agent],
            output_file='improvements.md',
            verbose=True
        )
    @crew
    def crew(self) -> Crew:	
        return Crew(
			agents=self.agents,
			tasks=self.tasks,
   			process=Process.sequential
			
		)