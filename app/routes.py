from fastapi import APIRouter
from services.data_preview.prompt_preview_class import Prompt_Preview
from services import azure_blob_uloader_instance
from services.utils import convertJsonToBytes , generate_timestamp
from database import saved_file_crud_sql_instance
from services import login_service_instance
from config import resource_url
import time
from fastapi import Request

# from fastapi.responses import StreamingResponse
# import time

router = APIRouter()


# @router.post("/api/v1/signup")
# def signup(username: str, password: str):
#     # Logic for sign up
#     return {"message": "User signed up successfully"}

@router.post("/api/v1/login")
def login(request: Request, username: str, password: str):
    user_authenticated = login_service_instance.login(username, password)
    if user_authenticated:
        request.session['username'] = username
        request.session['user_id'] = user_authenticated.id 
        return {"message": "Logged in successfully"}
    return {"message": "Invalid username or password"}, 401

@router.post("/api/v2/generate_example_prompts")
async def generate_example_prompts(topic: str):
    prompt_preview = Prompt_Preview()
    return prompt_preview.Generate_example_data(topic)

@router.post("/api/v2/generate_data")
async def generate_DataSet(request: Request,topic: str,number_records:int):
    start_time = time.time()
    prompt_preview = Prompt_Preview()
    json_file = prompt_preview.Generate_data(topic,number_records)
    json_file_bytes = convertJsonToBytes(json_file)
    file_path = request.session.get('username')+ "/" + generate_timestamp() + ".json"
    saved_file_crud_sql_instance.add(file_path,request.session.get('user_id'))
    azure_blob_uloader_instance.upload_files(file_path,json_file_bytes)
    print(f" finale time is  {time.time() - start_time}")
    return { "url" :resource_url + file_path }
    
@router.post("/logout")
def logout(request: Request):
    request.session.clear()
    return {"message": "Logged out successfully"}




