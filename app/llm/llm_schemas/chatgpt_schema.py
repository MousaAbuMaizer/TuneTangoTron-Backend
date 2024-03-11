from langchain_core.pydantic_v1 import BaseModel, Field, validator

class ChatgptSchema(BaseModel):
    role: str = Field(description="Represents the role of the message sender, whether it's the system, the user, or the assistant.")
    content: str = Field(description="Represents the actual content of the message sent by the system, the user, or the assistant.")