from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def ok() -> str:
    return "OK"