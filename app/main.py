from fastapi import FastAPI
import router.post as post

app = FastAPI()
app.include_router(post.router)

@app.get("/")
def ok() -> str:
    return "OK"