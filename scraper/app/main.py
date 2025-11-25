from fastapi import FastAPI
from app.schemas import ScrapeRequest, ScrapeResponse
from app.scraper import scrape_url

app = FastAPI(title="Scraper Service", version="0.1")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/scrape", response_model=ScrapeResponse)
async def scrape(req: ScrapeRequest):
    data = await scrape_url(req.url)
    return ScrapeResponse(url=req.url, data=data)
