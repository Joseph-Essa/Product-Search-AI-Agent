import os
from crewai.tools import tool 
from tavily import TavilyClient
from helpers.config import get_settings

class CrewaiTools:
    def __init__(self):
        self.settings = get_settings()
        
        self.search_client = TavilyClient(api_key=self.settings.TAVILY_API_KEY)
        self.search_engine_tool = self.create_search_tool()

    def create_search_tool(self):
        @tool
        def search_engine_tool(query: str):
            """Useful for search-based queries. Use this to find current information about any query related pages using a search engine"""
            return self.search_client.search(query)
        return search_engine_tool