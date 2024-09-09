from fastapi import FastAPI
from config import config
from mongodb import mongodb
import router.post as post
import router.auth as auth
from starlette.middleware.sessions import SessionMiddleware

def create_app():
    app = FastAPI()
    mongodb.connect()
    app.include_router(post.router)
    app.include_router(auth.router)
    app.add_middleware(SessionMiddleware, secret_key=config.session.SECRET_KEY)

    @app.get("/")
    def ok() -> str:
        return "OK"


    @app.get("/info")
    def info():
        return config.__dict__

    return app

app = create_app()
