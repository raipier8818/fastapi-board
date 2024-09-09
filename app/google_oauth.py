from authlib.integrations.starlette_client import OAuth
from config import config

oauth = OAuth()
oauth.register(
    name="google",
    client_id=config.google_oauth.GOOGLE_OAUTH_CLIENT_ID,
    client_secret=config.google_oauth.GOOGLE_OAUTH_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)
