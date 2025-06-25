from crewai import Crew, Process
from agents.search_queries_agent import search_queries_recommendation_agent
from tasks.search_queries_task import search_queries_recommendation_task
from crews.base import company_context


search_queries_crew = Crew(
    agents=[
        search_queries_recommendation_agent,
    ],
    tasks=[
        search_queries_recommendation_task,
    ],
    process=Process.sequential,
    knowledge_sources=[company_context]
)