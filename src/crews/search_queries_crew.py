from crewai import Crew, Process
from agents.search_queries_agent import search_queries_recommendation_agent
from tasks.search_queries_task import search_queries_recommendation_task
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

about_company = (
    "JEBE is a company that provides AI solutions to help websites "
    "refine their search and recommendation systems."
)

company_context = StringKnowledgeSource(content=about_company)


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