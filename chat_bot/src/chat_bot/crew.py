from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ChatBot():
    """ChatBot crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    # Create a knowledge source
    content = "Users name is Akshit. He is 24 years old and lives in Bengaluru, India"
    string_source = StringKnowledgeSource(content=content)
    pdf_source = PDFKnowledgeSource(
    file_paths=["story_book.pdf"]
)
    

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def helpful_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config['helpful_assistant'], # type: ignore[index]
            verbose=True
        )

    @task
    def helpful_assistant_task(self) -> Task:
        return Task(
            config=self.tasks_config['helpful_assistant_task'], # type: ignore[index]
        )

    

    @crew
    def crew(self) -> Crew:
        """Creates the ChatBot crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[self.string_source, self.pdf_source], # Add your knowledge sources here
            
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
