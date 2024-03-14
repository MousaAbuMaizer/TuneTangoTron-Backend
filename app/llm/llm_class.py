from langchain_openai import AzureChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from llm_schemas.langchain_schema import LangChainArraySchema , LangChainSchema
from prompt import full_data_generation_template
# from langchain.globals import set_debug
# set_debug(True)
# from langchain.globals import set_verbose
# set_verbose(True)


class GenerateSyntheticData:

    def __init__(self, azure_llm: AzureChatOpenAI):
        self.azure_llm = azure_llm

    def generate_data(self, topic: str, instructions: str, prefix: str, example: str, number_of_records: int):
        output_parser = PydanticOutputParser(pydantic_object=LangChainArraySchema)
        preview_prompt = PromptTemplate(template=full_data_generation_template,
                                        input_variables=["topic", "instructions", "prefix", "number_of_records",
                                                         "example"],
                                        partial_variables={"prompt_format": output_parser.get_format_instructions()})

        previewed_data_chain = preview_prompt | self.azure_llm | output_parser

        preview_prompt_response = previewed_data_chain.invoke(
            {'topic': topic, 'instructions': instructions, 'prefix': prefix, 'number_of_records': number_of_records,
             'example': example})

        print(preview_prompt_response)



AZURE_API_KEY_MAIN = "6edbfb029e8c4a0c8a13e065c3c76553"
AZURE_END_POINT_MAIN = "https://vidjalsa.openai.azure.com/openai/deployments/VidJalsa/chat/completions?api-version=2024-02-15-preview"

azure_llm = AzureChatOpenAI(
    api_key=AZURE_API_KEY_MAIN,
    model="gpt-4-1106-preview",
    openai_api_version="2023-07-01-preview",
    azure_endpoint=AZURE_END_POINT_MAIN,
    temperature=0.55
)

GenerateSyntheticData = GenerateSyntheticData(azure_llm)
GenerateSyntheticData.generate_data(
    topic= "car",
    instructions= """
    the dataset should have Systemmessage, HumanMessage and AssistantMessage. the SystemMessage should be "you are a useful chatbot requeired to answer questions about the history of the world" and the HumanMessage should the a query about the history of the world  and the AssistantMessage is the bot response on that query.
    """,
    prefix= "",
    example= """
    {"SystemMessage": " you are a useful chatbot requeired to answer questions about the history of the world", 
    "HumanMessage": "what is the history of the world", 
    "AssistantMessage": "The history of the world is the history of humanity, as determined from archaeology, anthropology, genetics, linguistics, and other disciplines; and, for periods since the invention of writing, from recorded history and from secondary sources and studies."}
    """,
    number_of_records= 5
)
