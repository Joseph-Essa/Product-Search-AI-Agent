from crews.config import CREW_CONFIGS
from crews.factory import CrewFactory
from helpers.crew_importer import dynamic_import

crew_registry = {}

for name, config in CREW_CONFIGS.items():
    agents = [dynamic_import(f"agents.{a}") for a in config["agents"]]
    tasks = [dynamic_import(f"tasks.{t}") for t in config["tasks"]]
    crew = CrewFactory.create_crew(agents, tasks, max_rpm=config.get("max_rpm"))
    crew_registry[name] = crew
