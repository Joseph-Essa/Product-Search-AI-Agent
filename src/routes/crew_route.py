from fastapi import APIRouter
# from crews.registry import crew_registry
from models.input import InputModel
from crews.registry import crew_registry


crew_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1","crew"]
)

@crew_router.post("/{crew_name}")
async def crew_pipeline (crew_name: str, payload: InputModel) : 
    crew = crew_registry.get(crew_name)
    if not crew:
        return {"error": f"Crew '{crew_name}' not found"}
    results = crew.kickoff(inputs=payload.dict())
    return {
        "message": f"{crew_name} pipeline completed successfully.",
        "results": results
    }
