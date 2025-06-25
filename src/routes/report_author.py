from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.input import InputModel
from crews.report_author_crew import report_author_crew

report_author_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1","report_author"]
)

@report_author_router.post("/report_author")
async def report_author_pipeline(payload: InputModel):
    crew_results = report_author_crew.kickoff(inputs=payload.dict())
    
    return JSONResponse(
        status_code=200,
        content={
            "message": "report author completed successfully.",
            "result": crew_results.dict()
        }
    )