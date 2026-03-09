from fastapi import Header, HTTPException

API_KEY = "trade_secret_key"

def verify_api_key(api_key: str = Header(...)):

    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return api_key