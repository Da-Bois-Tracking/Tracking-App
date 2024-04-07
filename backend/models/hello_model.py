from pydantic import BaseModel


# HelloResponse model that extends the Pydantic BaseModel
class HelloResponse(BaseModel):
    message: str
