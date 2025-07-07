import os, httpx
from src.llm.base import load_yaml

_conf = load_yaml("config/model_config.yaml")["langgraph"]

async def generate_with_langgraph(prompt: str) -> str:
    api_key = os.getenv(_conf["api_key_env"])
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            _conf["endpoint"],
            headers={"Authorization": f"Bearer {api_key}"},
            json={"query": prompt}
        )
        resp.raise_for_status()
        return resp.json().get("data", {}).get("response", "")
