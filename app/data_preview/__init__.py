from fastapi import HTTPException

from error_handling import initialize_azure_chat_openai

try:
    azure_llm = initialize_azure_chat_openai()
except HTTPException as e:
    print(e)
