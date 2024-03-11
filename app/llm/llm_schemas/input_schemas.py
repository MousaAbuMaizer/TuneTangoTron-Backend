from pydantic import BaseModel
from typing import List

class Topic(BaseModel):
    topic: str

class Instructions(BaseModel):
    instructions: str

class Number(BaseModel):
    number: int
    
class Example(BaseModel):
    example: List[dict]

class Prefix(BaseModel):
    prefix: str