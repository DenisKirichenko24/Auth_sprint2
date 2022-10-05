import os
from datetime import datetime, timezone
from dotenv import load_dotenv
from functools import wraps
import time
from flask import request, jsonify
from redis import Redis

load_dotenv()

r = Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"),  # type: ignore
          db=0, password=os.getenv("REDIS_PASSWORD"))  # type: ignore


def utc_now():
    """Current UTC date and time"""
    return datetime.now(timezone.utc)


def rate_limit(limit=10, interval=60, shared_limit=True, key_prefix="rl"):
    def rate_limit_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            t = int(time.time())
            closest_minute = t - (t % interval)
            if shared_limit:
                key = "%s:%s:%s" % (key_prefix, request.remote_addr, closest_minute)
            else:
                key = "%s:%s:%s.%s:%s" % (key_prefix, request.remote_addr,
                                          f.__module__, f.__name__, closest_minute)
            current = r.get(key)

            if current and int(current) > limit:
                retry_after = interval - (t - closest_minute)
                resp = jsonify({
                    'code': 429,
                    "message": "Too many requests. Limit %s in %s seconds" % (limit, interval)
                })
                resp.status_code = 429
                resp.headers['Retry-After'] = retry_after
                return resp
            else:
                pipe = r.pipeline()
                pipe.incr(key, 1)
                pipe.expire(key, interval + 1)
                pipe.execute()

                return f(*args, **kwargs)

        return wrapper

    return rate_limit_decorator
