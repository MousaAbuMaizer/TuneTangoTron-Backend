from pydantic import BaseModel
from typing import Any, Dict, Optional

class LoginRequest(BaseModel):
    username: str
    password: str

class GenerateRequest(BaseModel):
    topic: str
    instructions: str
    prefix: str
    examples: str
    number_records: int
    formatChoice: str
    customFormat: Optional[Dict[str, Any]] = None