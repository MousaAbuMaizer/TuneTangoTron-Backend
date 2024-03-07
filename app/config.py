import configparser
from langchain_openai import AzureOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

config = configparser.ConfigParser()

config.read("config.ini")

AZURE_API_KEY = config["AZURE"]["AZURE_API_KEY_MAIN"]

AZURE_ENDPOINT = config["AZURE"]["AZURE_END_POINT_MAIN"]


AZURE_BLOB_CONN = os.getenv("AZURE_BLOB_CONN")
AZURE_BLOB_CONTAINER_NAME = os.getenv("AZURE_BLOB_CONTAINER_NAME")
resource_url = os.getenv("resource_url")
azure_llm = AzureOpenAI(api_key= AZURE_API_KEY, azure_endpoint= AZURE_ENDPOINT, api_version="2023-07-01-preview", temperature= 0.6)