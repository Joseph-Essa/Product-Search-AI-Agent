from crewai import LLM
from helpers.config import get_settings

class LLMClient:
    def __init__(self):
        self.settings = get_settings()
        self.initialize_llm()

    def initialize_llm(self):
        return LLM(
            model=self.settings.LLM_MODEL_ID, 
            temperature=self.settings.LLM_MODEL_TEMPERATURE
        )