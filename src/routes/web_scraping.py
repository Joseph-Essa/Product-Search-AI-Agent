from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.input import InputModel
from crews.web_scraping_crew import web_scraping_crew

web_scraping_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1","web_scraping"]
)

@web_scraping_router.post("/web_scraping")
async def web_scraping_pipeline(payload: InputModel):
    crew_results = web_scraping_crew.kickoff(inputs=payload.dict())
    
    return JSONResponse(
        status_code=200,
        content={
            "message": "Search engine completed successfully.",
            "result": crew_results.dict()
        }
    )