from fastapi import FastAPI
from prompt_preview_class import Prompt_Preview
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/v2/generate_example_prompts")
async def generate_example_prompts(topic: str):
    prompt_preview = Prompt_Preview()
    return prompt_preview.Generate_example_data(topic)

@app.post("/api/v2/generate_data")
async def generate_DataSet(topic: str,number_records:int):
    prompt_preview = Prompt_Preview()
    return prompt_preview.Generate_data(topic,number_records)

