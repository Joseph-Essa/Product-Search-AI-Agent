import agentops
from helpers.config import get_settings

class AgentOpsClient:
    
    def __init__(self):
        
        self.settings = get_settings()
        self._initialize_agentops()

    def _initialize_agentops(self):
        
        agentops.init(
            api_key=self.settings.AGENTOPS_API_KEY,
            skip_auto_end_session=True,
            default_tags=['crewai']
        )

    def start_session(self):
        pass

    def end_session(self):
        
        agentops.end_trace()

