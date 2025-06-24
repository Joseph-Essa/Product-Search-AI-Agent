from enum import Enum

class AgentMessages(str, Enum):
    SEARCH_QUERIES_SUCCESS = "Search queries recommendations generated successfully."
    # RESEARCH_SUCCESS = "Research completed successfully."
    # WRITING_SUCCESS = "Writing task completed successfully."
    # REVIEW_SUCCESS = "Review completed successfully."
    AGENT_FAILED = "Agent task failed."