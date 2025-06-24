import os
from crewai import Task
from helpers.resources import create_agent_output_dir
from helpers.enums import AgentNames
from models.search_queries import SuggestedSearchQueries
from agents.search_queries_agent import search_queries_recommendation_agent


output_dir = create_agent_output_dir(AgentNames.SEARCH_QUERIES_RECOMMENDATION_AGENT.value)


search_queries_recommendation_task = Task(
    description="\n".join([
        "JEBE is looking to buy {product_name} at the best prices (value for a price strategy).",
        "The company targets any of these websites to buy from: {websites_list}.",
        "The company wants to reach all available products on the internet for later comparison.",
        "The stores must sell the product in {country_name}.",
        "Generate at maximum {no_keywords} queries.",
        "The search keywords must be in {language} language.",
        "Keywords must contain specific brands, types or technologies. Avoid general keywords.",
        "The search query must reach an ecommerce webpage for a product, not a blog or listing page."
    ]),
    expected_output="A JSON object containing a list of suggested search queries.",
    output_json=SuggestedSearchQueries,
    output_file=os.path.join(output_dir, "step_1_suggested_search_queries.json"),
    agent=search_queries_recommendation_agent
)