from fastapi import FastAPI
from prompt_preview_class import Prompt_Preview
from starlette.middleware.cors import CORSMiddleware
from error_handling import handle__format_prompt_api_errors

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@handle__format_prompt_api_errors
@app.post("/api/v1/generate_example_prompts")
async def generate_example_prompts(topic: str ,prompt_format:str):
    prompt_preview = Prompt_Preview()
    return prompt_preview.Generate_example_prompts(topic,prompt_format)
