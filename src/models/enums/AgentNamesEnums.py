from enum import Enum


class AgentNames(str, Enum):
    SEARCH_QUERIES_AGENT = "Search_Queries_Agent"
    SEARCH_ENGINE_AGENT = "Search_Engine_Agent"
    WEB_SCRAPING_AGENT = "Web_Scraping_Agent"
    REPORT_AUTHOR_AGENT = "Report_Author_Agent"