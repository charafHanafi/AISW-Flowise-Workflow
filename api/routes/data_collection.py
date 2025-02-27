from fastapi import FastAPI
import requests

app = FastAPI()

TWITTER_API = "https://api.twitter.com/2/tweets/search"
HEADERS = {"Authorization": "Bearer YOUR_TWITTER_API_KEY"}

@app.get("/api/data-collect")
def collect_insurance_data(query: str = "Moroccan insurance"):
    response = requests.get(TWITTER_API, headers=HEADERS, params={"query": query})
    return {"status": "success", "data": response.json()}

