
from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()
API_KEY = os.getenv("ANTHROPIC_API_KEY")

@app.post("/josi")
async def josi_endpoint(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    headers = {
    "x-api-key": API_KEY,
    "content-type": "application/json",
    "anthropic-version": "2023-06-01"
}

    payload = {
        "model": "claude-3-opus-20240229",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }

    response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)
    return response.json()
