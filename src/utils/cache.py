import os, hashlib, json
from functools import wraps

CACHE_DIR = "data/cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def disk_cache(fn):
    @wraps(fn)
    async def wrapped(prompt: str, *args, **kwargs):
        key = hashlib.sha256(prompt.encode()).hexdigest()
        path = os.path.join(CACHE_DIR, key + ".json")
        if os.path.exists(path):
            return json.load(open(path))["response"]
        resp = await fn(prompt, *args, **kwargs)
        with open(path, "w") as f:
            json.dump({"response": resp}, f)
        return resp
    return wrapped
