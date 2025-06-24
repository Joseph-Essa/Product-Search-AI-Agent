from crewai import Crew, Process
from agents.search_queries_agent import search_queries_recommendation_agent
from agents.search_engine_agent import search_engine_agent
from tasks.search_queries_task import search_queries_recommendation_task
from tasks.search_engine_task import search_engine_task
from crews.base import company_context


search_engine_crew = Crew(
    agents=[
        search_queries_recommendation_agent,
        search_engine_agent,
    ],
    tasks=[
        search_queries_recommendation_task,
        search_engine_task,
    ],
    process=Process.sequential,
    knowledge_sources=[company_context],
)