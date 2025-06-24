from enum import Enum


class AppMessages(str, Enum):
    WELCOME = "Hello All"
    HEALTHY = "API is healthy and running."
    ERROR_GENERIC = "An unexpected error occurred. Please try again."
    NOT_FOUND = "Resource not found."
    INVALID_INPUT = "Invalid input provided."


class AgentNames(str, Enum):
    SEARCH_QUERIES_RECOMMENDATION_AGENT = "search_queries_recommendation_agent"
    # RESEARCHER = "researcher"
    # WRITER = "writer"
    # REVIEWER = "reviewer"

class AgentMessages(str, Enum):
    SEARCH_QUERIES_SUCCESS = "Search queries recommendations generated successfully."
    # RESEARCH_SUCCESS = "Research completed successfully."
    # WRITING_SUCCESS = "Writing task completed successfully."
    # REVIEW_SUCCESS = "Review completed successfully."
    AGENT_FAILED = "Agent task failed."