from enum import Enum


class AgentNames(str, Enum):
    SEARCH_QUERIES_RECOMMENDATION_AGENT = "search_queries_recommendation_agent"
    SEARCH_ENGINE_AGENT = "Search_Engine_Agent"
    WEB_SCRAPING_AGENT = "Web Scraping Agent"
    REPORT_AUTHOR_AGENT = "report_author_agent"