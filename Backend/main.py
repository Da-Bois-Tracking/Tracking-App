from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Greetings"])
def Hello():
    return {"Hello": "World"}
