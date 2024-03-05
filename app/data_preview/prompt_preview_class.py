from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from preview_prompt import preview_generated_data_prompt
from fastapi import HTTPException
from __init__ import azure_llm
output_parser = StrOutputParser()
class Prompt_Preview:
    """this class containt a function that takes input and generate 5 prompts based on a certain topic"""
    def Generate_example_prompts(self, topic: str) -> str:
            """
            Generate example prompts based on the provided topic.

            Parameters:
            - topic (str): The topic for which prompts will be generated.

            Returns:
            - example_prompt (str): Example prompt generated based on the topic.

            Raises:
            - HTTPException: If there was an issue during prompt generation.
            """

            preview_prompt = PromptTemplate(template=preview_generated_data_prompt, input_variables=["topic"])
            previewed_data_chain = preview_prompt | azure_llm | output_parser

            try:
                preview_prompt_response = previewed_data_chain.invoke({'topic': topic})
                preview_prompt_formated_response = preview_prompt_response.replace('\\n', '\n')
                print(preview_prompt_formated_response)
                return preview_prompt_formated_response
            except HTTPException as e:
                raise e
        