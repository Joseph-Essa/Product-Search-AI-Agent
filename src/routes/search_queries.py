from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.input import InputModel
from crews.search_queries_crew import search_queries_crew

search_queries_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1","SearchQueries"]
)

@search_queries_router.post("/SearchQueries")
async def search_queries_pipeline(payload: InputModel):
    crew_results = search_queries_crew.kickoff(inputs=payload.dict())
    
    return JSONResponse(
        status_code=200,
        content={
            "message": "Search queries pipeline completed successfully.",
            "result": crew_results.dict()
        }
    )