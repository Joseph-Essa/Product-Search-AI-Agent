from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    APP_NAME: str 
    APP_VERSION: str
    AGENTOPS_API_KEY: str 
    # GEMINI_API_KEY : str 
    TAVILY_API_KEY : str 
    LLM_MODEL_ID : str
    LLM_MODEL_TEMPERATURE : float
    SCRAPEGRAPHAI_API_KEY : str
    GROQ_API_KEY : str
    class Config:
        env_file = ".env"

def get_settings () : 
    return Settings()
