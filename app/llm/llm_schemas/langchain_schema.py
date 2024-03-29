from langchain_core.pydantic_v1 import BaseModel, Field, validator
from typing import List, Optional

class LangChainSchema(BaseModel):


    SystemMessage: str = Field(
        description="Describes the MAIN ROLE and behavior or action or the tone performed by the AI system"
    )
    HumanMessage: str = Field(
        description="Represents a message sent by a user seeking information, clarification, or engaging in conversation."
    )
    AssistantMessage: str = Field(
        description="Represents a response generated by the AI assistant in reply to a user's query or input."
    )



class LangChainArraySchema(BaseModel):
    messages: List[LangChainSchema] = Field(
        ..., description="An array of LangChainSchema objects."
    )
