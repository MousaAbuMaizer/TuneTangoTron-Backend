from langchain_openai import AzureChatOpenAI
import os


AZURE_API_KEY = os.getenv('AZURE_API_KEY')
if not AZURE_API_KEY:
    raise EnvironmentError("Azure API key (AZURE_API_KEY) not found in environment variables.")

AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT')
if not AZURE_ENDPOINT:
    raise EnvironmentError("Azure endpoint (AZURE_ENDPOINT) not found in environment variables.")


try:
    azure_llm = AzureChatOpenAI(api_key=AZURE_API_KEY, model="gpt-4",
                                openai_api_version="2023-07-01-preview",
                                azure_endpoint=AZURE_ENDPOINT, temperature=0.55)
except Exception as e:
    raise RuntimeError(f"Failed to initialize Azure Chat OpenAI instance: {e}")
