import requests

def get_market_news(sector: str):

    query = f"India {sector} sector market trends"

    url = "https://api.duckduckgo.com/"

    params = {
        "q": query,
        "format": "json",
        "no_redirect": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        topics = data.get("RelatedTopics", [])

        news_list = []

        for item in topics:
            if isinstance(item, dict) and "Text" in item:
                news_list.append(item["Text"])

        if not news_list:
            return f"No recent market news found for {sector} sector."

        return "\n".join(news_list[:5])

    except Exception:
        return f"Unable to fetch market data for {sector}."