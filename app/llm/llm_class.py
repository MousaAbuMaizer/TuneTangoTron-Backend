from langchain_openai import AzureChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from llm.llm_schemas.langchain_schema import LangChainArraySchema , LangChainSchema
from llm.prompt import full_data_generation_template
from langchain.globals import set_debug
set_debug(True)
from langchain.globals import set_verbose
set_verbose(True)


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
        return preview_prompt_response.json()

