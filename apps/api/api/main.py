from fastapi import FastAPI

app = FastAPI(title="Web Event Platform API", description="It's a REST API", version="0.0.1")


@app.get("/")
def hello():
    return {"message": "Hello world!"}
