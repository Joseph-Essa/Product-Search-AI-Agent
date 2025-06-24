import os
from crewai import Task
from helpers.resources import create_agent_output_dir
from models.enums.AgentNamesEnums import AgentNames
from models.search_engine import AllSearchResults
from agents.search_engine_agent import search_engine_agent

output_dir = create_agent_output_dir(AgentNames.SEARCH_ENGINE_AGENT.value)

search_engine_task = Task(
    description="\n".join([
        "The task is to search for products based on the suggested search queries.",
        "You have to collect results from multiple search queries.",
        "Do not retrieve any website link except this websites:{websites_list} "
        "Ignore any susbicious links or not an ecommerce single product website link.",
        "Ignore any search results with confidence score less than ({score_th}) .",
        "The search results will be used to compare prices of products from different websites.",
    ]),
    expected_output="A JSON object containing the search results.",
    output_json=AllSearchResults,
    output_file=os.path.join(output_dir, "step_2_search_results.json"),
    agent=search_engine_agent
)