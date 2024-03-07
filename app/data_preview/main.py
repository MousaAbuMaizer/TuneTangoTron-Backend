from fastapi import FastAPI, HTTPException
from prompt_preview_class import Prompt_Preview
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint for generating example prompts
@app.post("/api/v3/generate_example_prompts")
async def generate_data_samples(topic: str, data_format: str = 'LangChainSchema'):
    prompt_preview = Prompt_Preview()
    if data_format not in ['ChatgptSchema', 'LangChainSchema']:
        raise HTTPException(status_code=400, detail="Invalid data_format. Choose either 'ChatgptSchema' or 'LangChainSchema'")
    
    return prompt_preview.Generate_example_data(topic,data_format)

# Endpoint for generating data set
@app.post("/api/v3/generate_data")
async def generate_DataSet(topic: str, number_records: int, data_format: str = 'LangChainSchema'):
    prompt_preview = Prompt_Preview()
    if data_format not in ['Chatgptformat', 'Langchainformat']:
        raise HTTPException(status_code=400, detail="Invalid data_format. Choose either 'Chatgptformat' or 'Langchainformat'")
    
    return prompt_preview.Generate_data(topic, number_records,data_format)
