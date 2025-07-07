import time
from functools import wraps

def rate_limit(calls_per_minute: int):
    interval = 60.0 / calls_per_minute
    def decorator(fn):
        last = {"t": 0.0}
        @wraps(fn)
        async def wrapped(*args, **kwargs):
            elapsed = time.time() - last["t"]
            if elapsed < interval:
                await asyncio.sleep(interval - elapsed)
            res = await fn(*args, **kwargs)
            last["t"] = time.time()
            return res
        return wrapped
    return decorator
