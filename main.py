from fastapi import FastAPI, Depends, HTTPException, Request
from auth import verify_api_key
from data_collector import get_market_news
from ai_analyzer import analyze_market
from report_generator import create_markdown_report
from rate_limiter import limiter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI(title="Trade Opportunities API")

sessions = {}

@app.get("/analyze/{sector}")
@limiter.limit("10/minute")
async def analyze_sector(
    request: Request,
    sector: str,
    api_key: str = Depends(verify_api_key)
):

    try:

        logger.info(f"Received request for sector: {sector}")

        if not sector.isalpha():
            raise HTTPException(status_code=400, detail="Invalid sector name")

        sessions[api_key] = sessions.get(api_key, 0) + 1

        news = get_market_news(sector)

        logger.info("Market data collected")

        analysis = analyze_market(sector, news)

        logger.info("AI analysis completed")

        report = create_markdown_report(sector, analysis)

        file_name = f"reports/{sector}_report.md"

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(report)
        
        return {
            "sector": sector,
            "session_requests": sessions[api_key],
            "report": report
        }

    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))
