from crewai import Agent
from clients import LLMClient

basic_llm = LLMClient().initialize_llm()

search_queries_agent = Agent(
    role="Search Queries Recommendation Agent",
    goal="\n".join([
                "To provide a list of suggested search queries to be passed to the search engine.",
                "The queries must be varied and looking for specific items."
            ]),
    backstory="The agent is designed to help in looking for products by providing a list of suggested search queries to be passed to the search engine based on the context provided.",
    llm=basic_llm,
    verbose=True,
)
