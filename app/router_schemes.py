from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class TopicRequest(BaseModel):
    topic: str

class GenerateRequest(BaseModel):
    topic: str
    number_records: int
