# Trade Opportunities API

FastAPI service that analyzes Indian market sectors and generates
trade opportunity reports using Gemini AI.

## Features

* FastAPI backend
* AI market analysis
* Web data collection
* API key authentication
* Rate limiting
* Session tracking
* Markdown report generation

## Installation

pip install -r requirements.txt

## Activate Environment

.\.venv\Scripts\Activate

## Run Server

python -m uvicorn main:app --reload

## URL

http://127.0.0.1:8000/docs#/

## API Endpoint

GET /analyze/{sector}

Example:

/analyze/technology
/analyze/pharmaceuticals
/analyze/finance
/analyze/agriculture


Header:

api-key: trade_secret_key
