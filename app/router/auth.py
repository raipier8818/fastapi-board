from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse
from guard import local_auth_guard
from google_oauth import oauth

router = APIRouter(prefix="/auth")

@router.get("/google")
async def google_oauth(request:Request):
    redirect_url = request.url_for("google_callback")
    return await oauth.google.authorize_redirect(request, redirect_url)

@router.get("/google/callback", name="google_callback")
async def auth(request: Request):
    token:dict = await oauth.google.authorize_access_token(request)
    
    userinfo: dict = token.get("userinfo")
    ( email, name ) = userinfo.get("email"), userinfo.get("name")
    request.session["user"] = {"email": email, "name": name}
    return RedirectResponse(url="/post", status_code=302)

@router.get("/logout")
@local_auth_guard
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/", status_code=302)

@router.get("/profile")
@local_auth_guard
async def profile(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user
