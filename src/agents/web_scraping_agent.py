from crewai import Agent
from clients import LLMClient
from tools.crewai_tools import CrewaiTools


basic_llm = LLMClient().initialize_llm()
tools = CrewaiTools()


web_scraping_agent = Agent(
    role="Web scraping agent",
    goal="To extract details from any website",
    backstory="The agent is designed to help in looking for required values from any website url. These details will be used to decide which best product to buy.",
    llm=basic_llm,
    tools=[tools.web_scraping_tool],
    verbose=True,
)