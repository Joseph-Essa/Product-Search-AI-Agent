from crewai import Agent
from helpers.crewai_config import basic_llm

search_queries_recommendation_agent = Agent(
    role="Search Queries Recommendation Agent",
    goal="\n".join([
                "To provide a list of suggested search queries to be passed to the search engine.",
                "The queries must be varied and looking for specific items."
            ]),
    backstory="\n".join(["The agent is designed to help in looking for products" ,
                        "by providing a list of suggested search queries to be ",
                        "passed to the search engine based on the context provided."
                    ]),
    llm=basic_llm,
    verbose=True,
)
