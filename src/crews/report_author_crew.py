from crewai import Crew, Process
from agents.search_queries_agent import search_queries_recommendation_agent
from agents.search_engine_agent import search_engine_agent
from agents.web_scraping_agent import web_scraping_agent
from agents.report_author_agent import report_author_agent

from tasks.search_queries_task import search_queries_recommendation_task
from tasks.search_engine_task import search_engine_task
from tasks.web_scraping_task import web_scraping_task
from tasks.report_author_task import report_author_task

from crews.base import company_context

report_author_crew = Crew(
    agents=[
        search_queries_recommendation_agent,
        search_engine_agent,
        web_scraping_agent , 
        report_author_agent , 
    ],
    tasks=[
        search_queries_recommendation_task,
        search_engine_task,
        web_scraping_task ,
        report_author_task,
    ],
    process=Process.sequential,
    knowledge_sources=[company_context],
    max_rpm=60 ,
)