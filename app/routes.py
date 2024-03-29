from fastapi import APIRouter, HTTPException, Request
from router_schemes import GenerateRequest, LoginRequest
from services.data_preview.prompt_preview_class import Prompt_Preview,preview_prompts_v2
from services import azure_blob_uloader_instance
from services.utils import convertJsonToBytes , generate_timestamp
from database import saved_file_crud_sql_instance
from services import login_service_instance
from config import resource_url
from services.llm_service import LLMGenerateService
# from fastapi.responses import StreamingResponse
# import time

router = APIRouter()

@router.post("/api/v1/login")
# def login(session_request: Request,request: LoginRequest):
def login(request: LoginRequest):
    user_authenticated = login_service_instance.login(request.username, request.password)
    if user_authenticated:
        # session_request.session['username'] = request.username
        # session_request.session['user_id'] = user_authenticated.id 
        # print(session_request.session)
        return {"success": True}

# @router.post("/api/v2/generate_example_prompts")
# async def generate_example_prompts(request: TopicRequest):
#     print("TopicRequest", TopicRequest)
#     prompt_preview = Prompt_Preview()
#     return prompt_preview.Generate_example_data(request.topic)


@router.post("/api/v2/generate_data")
async def generate_dataSet(request: GenerateRequest):
    llm_generate_service = LLMGenerateService()

    # json_file =llm_generate_service.generate_data(
    #     request.topic,
    #     """the dataset should have Systemmessage, HumanMessage and AssistantMessage. the SystemMessage should be "you are a useful chatbot requeired to answer questions about the history of the world" and the HumanMessage should the a query about the history of the world  and the AssistantMessage is the bot response on that query.""",
    #     "nan",
    #     """ {"SystemMessage": " you are a useful chatbot requeired to answer questions about the history of the world", 
    # "HumanMessage": "what is the history of the world", 
    # "AssistantMessage": "The history of the world is the history of humanity, as determined from archaeology, anthropology, genetics, linguistics, and other disciplines; and, for periods since the invention of writing, from recorded history and from secondary sources and studies."} """,
    #     5,
    #     request.formatChoice
    # )

    json_file =llm_generate_service.generate_data(
        request.topic,
        request.instructions,
        request.prefix,
        request.examples,
        request.number_records,
        request.formatChoice
    )
    json_file_bytes = convertJsonToBytes(json_file)
    # file_path = session_request.session.get('username') + generate_timestamp() + ".json"
    file_path = "hamza" + generate_timestamp() + ".json"
    # saved_file_crud_sql_instance.add(file_path, session_request.session.get('user_id'))
    saved_file_crud_sql_instance.add(file_path, 1)
    azure_blob_uloader_instance.upload_files(file_path, json_file_bytes)
    return {"url": resource_url + file_path}


@router.post("/api/v2/priview_data")
async def generate_dataSet(request: GenerateRequest):
    llm_generate_service = LLMGenerateService()

    # json_file =llm_generate_service.generate_data(
    #     request.topic,
    #     """the dataset should have Systemmessage, HumanMessage and AssistantMessage. the SystemMessage should be "you are a useful chatbot requeired to answer questions about the history of the world" and the HumanMessage should the a query about the history of the world  and the AssistantMessage is the bot response on that query.""",
    #     "nan",
    #     """ {"SystemMessage": " you are a useful chatbot requeired to answer questions about the history of the world", 
    # "HumanMessage": "what is the history of the world", 
    # "AssistantMessage": "The history of the world is the history of humanity, as determined from archaeology, anthropology, genetics, linguistics, and other disciplines; and, for periods since the invention of writing, from recorded history and from secondary sources and studies."} """,
    #     5,
    #     request.formatChoice
    # )

    json_file =llm_generate_service.generate_data(
        request.topic,
        request.instructions,
        request.prefix,
        request.examples,
        5,
        request.formatChoice
    )
    return json_file

# @router.post("/api/v2/generate_data")
# async def generate_dataSet(request: GenerateRequest):
#     time.sleep(5)
#     # prompt_preview = Prompt_Preview()
#     # json_file = prompt_preview.Generate_data(request.topic, request.number_records)
#     # json_file_bytes = convertJsonToBytes(json_file)
#     # # file_path = session_request.session.get('username') + generate_timestamp() + ".json"
#     # file_path = "hamza" + generate_timestamp() + ".json"
#     # # saved_file_crud_sql_instance.add(file_path, session_request.session.get('user_id'))
#     # saved_file_crud_sql_instance.add(file_path, 1)
#     # azure_blob_uloader_instance.upload_files(file_path, json_file_bytes)
#     return {"url": "resource_url + file_path"}





# # Endpoint for generating example prompts
# @router.post("/api/v3/generate_example_data_v2")
# async def generate_data_samples(request: TopicRequest):
#     prompt_preview = preview_prompts_v2()
#     # if data_format not in ['ChatgptSchema', 'LangChainSchema']:
#     #     raise HTTPException(status_code=400, detail="Invalid data_format. Choose either 'ChatgptSchema' or 'LangChainSchema'")
    
#     return prompt_preview.Generate_example_data_v2(request.topic,'LangChainSchema')

# # Endpoint for generating data set
# @router.post("/api/v3/generate_data_v2")
# async def generate_DataSet_v2(request: GenerateRequest):
#     prompt_preview = preview_prompts_v2()
#     # if data_format not in ['ChatgptSchema', 'LangChainSchema']:
#     #     raise HTTPException(status_code=400, detail="Invalid data_format. Choose either 'ChatgptSchema' or 'LangChainSchema'")
    
#     return prompt_preview.Generate_data_v2(request.topic, request.number_records,'LangChainSchema')

# @router.post("/api/v1/signup")
# def signup(username: str, password: str):
#     # Logic for sign up
#     return {"message": "User signed up successfully"}

# @router.post("/logout")
# def logout(session_request: Request):
#     session_request: session_request.session.clear()
#     return {"message": "Logged out successfully"}
