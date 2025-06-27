from crewai import Crew, Process
from crews.base import company_context

class CrewFactory:
    @staticmethod
    def create_crew(agents, tasks, max_rpm=None):
        return Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential,
            knowledge_sources=[company_context],
            **({"max_rpm": max_rpm} if max_rpm else {})
        )