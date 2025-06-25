import os
from crewai import Task
from helpers.resources import create_agent_output_dir
from models.enums.AgentNamesEnums import AgentNames
from models.web_scraping import AllExtractedProducts
from agents.web_scraping_agent import web_scraping_agent

output_dir = create_agent_output_dir(AgentNames.WEB_SCRAPING_AGENT.value)


web_scraping_task = Task(
    description="\n".join([
        "The task is to extract product details from any ecommerce store page url.",
        "The task has to collect results from multiple pages urls.",
        "Collect the best {top_recommendations_no} products from the search results.",
    ]),
    expected_output="A JSON object containing products details",
    output_json=AllExtractedProducts,
    output_file=os.path.join(output_dir, "step_3_search_results.json"),
    agent=web_scraping_agent
)