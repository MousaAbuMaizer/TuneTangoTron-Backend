from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from preview_prompt import preview_generated_data_prompt_langchain_format , preview_generated_data_prompt_openai_format
from fastapi import HTTPException
from __init__ import azure_llm
from error_handling import handle_format_error
import json

output_parser = StrOutputParser()
class Prompt_Preview:
    """this class containt a function that takes input and generate 5 prompts based on a certain topic"""
    def Generate_example_prompts(self, topic: str , prompt_format:str) -> str:
            """
            Generate example prompts based on the provided topic.

            Parameters:
            - topic (str): The topic for which prompts will be generated.
            - prompt_format (str): The format of the prompt to be generated.

            Returns:
            - example_prompt (str): Example prompt generated based on the topic.

            Raises:
            - HTTPException: If there was an issue during prompt generation.
            """
            # Define the mapping of the format of the prompt to the function that will generate the prompt.
            format_mapping = {
        'openai': preview_generated_data_prompt_openai_format,
        'langchain': preview_generated_data_prompt_langchain_format
    }

            handle_format_error(prompt_format, format_mapping)
            preview_prompt = PromptTemplate(template=format_mapping[prompt_format], input_variables=["topic"])
            previewed_data_chain = preview_prompt | azure_llm | output_parser

            try:
                preview_prompt_response = previewed_data_chain.invoke({'topic': topic})
                preview_prompt_formated_response = preview_prompt_response.replace('\\n', '\n')
                 # Convert the response to a JSON object
                json_response = json.dumps(preview_prompt_formated_response)
                print(json_response)
                return json_response
                

            except HTTPException as e:
                 raise HTTPException(status_code=400, detail="There was an error while generating your Data'.")
        