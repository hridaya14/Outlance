import logging
import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from src.routers import ping


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan for the API.
    """

    logger.info("Starting RAG API...")
    logger.info("Started API Server")

    yield

    logger.info("Shutting down API")

app = FastAPI(
    title="arXiv Paper Curator API",
    description="Personal arXiv CS.AI paper curator with RAG capabilities",
    version=os.getenv("APP_VERSION", "0.1.0"),
    lifespan=lifespan,
)

# Routers
app.include_router(ping.router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
