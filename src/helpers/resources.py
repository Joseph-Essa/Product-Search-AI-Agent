import os

ROOT_OUTPUT_DIR = "./assets"
os.makedirs(ROOT_OUTPUT_DIR, exist_ok=True)

def create_agent_output_dir(agent_name: str) -> str:
    agent_dir = os.path.join(ROOT_OUTPUT_DIR, str(agent_name))
    os.makedirs(agent_dir, exist_ok=True)
    return agent_dir

def get_agent_output_file(agent_name: str, filename: str) -> str:
    agent_dir = create_agent_output_dir(agent_name)
    return os.path.join(agent_dir, filename)