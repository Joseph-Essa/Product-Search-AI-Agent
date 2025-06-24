from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.input import InputModel
from crews.search_engine_crew import search_engine_crew

search_engine_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1","SearchEngine"]
)

@search_engine_router.post("/search_engine")
async def search_engine_pipeline(payload: InputModel):
    crew_results = search_engine_crew.kickoff(inputs=payload.dict())
    
    return JSONResponse(
        status_code=200,
        content={
            "message": "Search engine completed successfully.",
            "result": crew_results.dict()
        }
    )