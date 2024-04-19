import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import items

app = FastAPI()

app.include_router(items.router, tags=["Items"])

origins = [
    "http://localhost:3000",
    os.environ.get("CORS_HOST", None),
]

# Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Greetings"])
def Hello():
    return {"Hello": "Friends"}
