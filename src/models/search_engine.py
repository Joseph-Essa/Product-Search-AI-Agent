from pydantic import BaseModel, Field
from typing import List

class SignleSearchResult(BaseModel):
    title: str
    url: str = Field(..., title="the page url")
    content: str
    score: float
    search_query: str

class AllSearchResults(BaseModel):
    results: List[SignleSearchResult]
