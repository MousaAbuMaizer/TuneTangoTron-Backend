from fastapi import HTTPException
from langchain_openai import AzureChatOpenAI
import os
from config import AZURE_API_KEY , AZURE_ENDPOINT


def handle_missing_api_key():
    if not AZURE_API_KEY:
        raise HTTPException(status_code=500, detail="Azure API key (AZURE_API_KEY) not found in environment variables.")

def handle_missing_endpoint():
    if not AZURE_ENDPOINT:
        raise HTTPException(status_code=500, detail="Azure endpoint (AZURE_ENDPOINT) not found in environment variables.")

def initialize_azure_chat_openai():
    handle_missing_api_key()
    handle_missing_endpoint()

    try:
        azure_llm = AzureChatOpenAI(
            api_key=AZURE_API_KEY,
            model="gpt-4-1106-preview",
            openai_api_version="2023-07-01-preview",
            azure_endpoint=AZURE_ENDPOINT,
            temperature=0.55
        )
        return azure_llm
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to initialize Azure Chat OpenAI instance: {str(e)}")


def handle_format_error(prompt_format, format_mapping):
    if prompt_format not in format_mapping:
        raise HTTPException(status_code=400, detail="Invalid format type. Expected 'openai' or 'langchain'.")
    
def handle__format_prompt_api_errors(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return wrapper