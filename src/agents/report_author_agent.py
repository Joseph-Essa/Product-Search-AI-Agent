from crewai import Agent
from clients import LLMClient

basic_llm = LLMClient().initialize_llm()

report_author_agent = Agent(
    role="Procurement Report Author Agent",
    goal="To generate a professional HTML page for the procurement report",
    backstory="The agent is designed to assist in generating a professional HTML page for the procurement report after looking into a list of products.",
    llm=basic_llm,
    verbose=True,
)