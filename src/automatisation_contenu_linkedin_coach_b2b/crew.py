import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
	ScrapeWebsiteTool
)






@CrewBase
class AutomatisationContenuLinkedinCoachB2bCrew:
    """AutomatisationContenuLinkedinCoachB2b crew"""

    
    @agent
    def analyste_tendances_b2b(self) -> Agent:

        
        return Agent(
            config=self.agents_config["analyste_tendances_b2b"],
            
            
            tools=[
				SerperDevTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def stratege_contenu_linkedin(self) -> Agent:

        
        return Agent(
            config=self.agents_config["stratege_contenu_linkedin"],
            
            
            tools=[
				ScrapeWebsiteTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def redacteur_posts_linkedin(self) -> Agent:

        
        return Agent(
            config=self.agents_config["redacteur_posts_linkedin"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def analyse_des_tendances_b2b(self) -> Task:
        return Task(
            config=self.tasks_config["analyse_des_tendances_b2b"],
            markdown=False,
            
        )
    
    @task
    def strategie_contenu_linkedin(self) -> Task:
        return Task(
            config=self.tasks_config["strategie_contenu_linkedin"],
            markdown=False,
            
        )
    
    @task
    def redaction_posts_linkedin(self) -> Task:
        return Task(
            config=self.tasks_config["redaction_posts_linkedin"],
            markdown=False,
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the AutomatisationContenuLinkedinCoachB2b crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
