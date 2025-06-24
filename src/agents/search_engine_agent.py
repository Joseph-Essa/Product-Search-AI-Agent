from crewai import Agent
from clients import LLMClient
from crewai.tools import tool 
from tavily import TavilyClient
from tools.crewai_tools import CrewaiTools


basic_llm = LLMClient().initialize_llm()
tools = CrewaiTools()

search_engine_agent = Agent(
    role="Search Engine Agent",
    goal="To search for products based on the suggested search query",
    backstory="The agent is designed to help in looking for products by searching for products based on the suggested search queries.",
    llm=basic_llm,
    verbose=True,
    tools=[tools.search_engine_tool]
)