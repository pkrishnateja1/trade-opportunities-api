from google import genai
import os
# Replace with your real key
client = genai.Client(api_key=("YOUR-API-KEY"))

def analyze_market(sector, news):

    prompt = f"""
You are a financial analyst.

Analyze the Indian {sector} sector using the following market information.

Data: {news}

Provide:

1. Market Overview
2. Key Companies
3. Recent Developments
4. Trade Opportunities
5. Risks

Format the response as markdown.
"""

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI analysis failed: {str(e)}"