import os
from crewai import Task
from helpers.resources import create_agent_output_dir
from models.enums.AgentNamesEnums import AgentNames
from models.search_queries import SuggestedSearchQueries
from agents.search_queries_agent import search_queries_recommendation_agent


output_dir = create_agent_output_dir(AgentNames.SEARCH_QUERIES_RECOMMENDATION_AGENT.value)


search_queries_recommendation_task = Task(
    description="\n".join([
        "JEBE is looking to buy {product_name} at the best prices (value for a price strategy)",
        "The campany target any of these websites to buy from: {websites_list}",
        "The retrieved results must contain the website name on the last of queries",
        "The retrieved results must not contain any special character",
        "The company wants to reach all available proucts on the internet to be compared later in another stage.",
        "The stores must sell the product in {country_name}",
        "Generate at maximum {no_keywords} queries.",
        "The search keywords must be in {language} language.",
        "Search keywords must contains specific brands, types or technologies. Avoid general keywords.",
        "The search query must reach an ecommerce webpage for product, and not a blog or listing page."
    ]),
    expected_output="A JSON object containing a list of suggested search queries.",
    output_json=SuggestedSearchQueries,
    output_file=os.path.join(output_dir, "step_1_suggested_search_queries.json"),
    agent=search_queries_recommendation_agent
)