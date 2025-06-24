import agentops
from helpers.config import get_settings

class AgentOpsClient:
    
    def __init__(self):
        
        self.settings = get_settings()
        self.initialize_agentops()

    def initialize_agentops(self):
        
        agentops.init(
            api_key=self.settings.AGENTOPS_API_KEY,
            skip_auto_end_session=True,
            default_tags=['crewai']
        )
