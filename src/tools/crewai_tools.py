import os
from crewai.tools import tool 
from tavily import TavilyClient
from helpers.config import get_settings
from scrapegraph_py import Client
import json
from models.web_scraping import SingleExtractedProduct

class CrewaiTools:
    def __init__(self):
        self.settings = get_settings()
        
        self.search_client = TavilyClient(api_key=self.settings.TAVILY_API_KEY)
        self.search_engine_tool = self.create_search_tool()
        
        self.scraping_client = Client(api_key=self.settings.SCRAPEGRAPHAI_API_KEY)
        self.web_scraping_tool = self.create_scraping_tool()
        

    def create_search_tool(self):
        @tool
        def search_engine_tool(query: str):
            """Useful for search-based queries. Use this to find current information about any query related pages using a search engine"""
            return self.search_client.search(query)
        return search_engine_tool
    
    def create_scraping_tool(self):
        @tool
        def web_scraping_tool(page_url: str ):
            """
            An AI Tool to help an agent to scrape a web page
            
            Example:
            web_scraping_tool(
                page_url="https://www.noon.com/egypt-en/fresh-portable-air-conditioner-that-runs-on-freon/Z2CD8B06CDE43D9EBD82CZ/p/?o=z2cd8b06cde43d9ebd82cz-1&shareId=b1f9b6fb-5c35-403d-af1e-3dfd90c25da9"
            )
            """
            results =self.scraping_client.smartscraper(
                website_url=page_url , 
                user_prompt=f"Extract ```\n{SingleExtractedProduct.schema_json()}```\n From the web page"
            )
            return {
                "page_url" : page_url , 
                "details" : results
            }
        return web_scraping_tool