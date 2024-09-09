from functools import wraps
from fastapi import HTTPException

def local_auth_guard(func):
    @wraps(func)
    async def wrapper(request, *args, **kwargs):
        user = request.session.get("user")
        if not user or not user.get("email") or not user.get("name"):
            raise HTTPException(status_code=401, detail="Not authenticated")
        return await func(request, *args, **kwargs)
    return wrapper