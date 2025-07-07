import os, httpx
from src.llm.base import load_yaml
from src.utils.rate_limiter import rate_limit

_conf = load_yaml("config/model_config.yaml")["openrouter"]

@rate_limit(calls_per_minute=60)
async def generate_with_openrouter(prompt: str) -> str:
    api_key = os.getenv(_conf["api_key_env"])
    
    payload = {
        "model": _conf["model"],
        "messages": [
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt}
        ],
        "temperature": _conf["temperature"]
    }
    headers = {"Authorization": f"Bearer {api_key}"}
    async with httpx.AsyncClient() as client:
        resp = await client.post(_conf["endpoint"], json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()
    return data["choices"][0]["message"]["content"]
