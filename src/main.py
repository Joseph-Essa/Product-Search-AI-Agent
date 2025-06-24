from fastapi import FastAPI
from clients import AgentOpsClient 
from routes import base
from routes import search_queries, search_engine
import agentops


app = FastAPI()
agent_ops_client = AgentOpsClient()

async def startup_span():
    print("Starting up...")
    agent_ops_client.initialize_agentops()
    print("AgentOps initialized")


async def shutdown_span():
    print("Shutting down...")
    agentops.end_trace()
    print("Shutdown complete")


app.on_event("startup")(startup_span)
app.on_event("shutdown")(shutdown_span)


app.include_router(base.base_router)
app.include_router(search_queries.search_queries_router)
app.include_router(search_engine.search_engine_router)

