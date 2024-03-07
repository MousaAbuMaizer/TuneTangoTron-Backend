from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from preview_prompt import preview_generated_data ,main_template
from langchain_core.output_parsers import JsonOutputParser
from fastapi import HTTPException
from __init__ import azure_llm
from error_handling import handle_format_error
import json
from Output_schemes import LangChainSchema
class Prompt_Preview:
    """this class containt a function that takes input and generate 5 prompts based on a certain topic"""
    def Generate_example_data(self, topic: str):
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

            output_parser = JsonOutputParser(pydantic_object=LangChainSchema)
            preview_prompt = PromptTemplate(template=preview_generated_data, input_variables=["topic"],
                                            partial_variables={"prompt_format":output_parser.get_format_instructions()})
            previewed_data_chain = preview_prompt | azure_llm | output_parser 

            try:
                preview_prompt_response = previewed_data_chain.invoke({'topic': topic})
                #preview_prompt_formated_response = preview_prompt_response.replace('\\n', '\n')
                print(preview_prompt_response)
                return preview_prompt_response
                # Convert the response to a JSON object
                #json_response = json.dumps(preview_prompt_formated_response)
                #print(json_response)
                #return json_response
                

            except HTTPException as e:
                 raise HTTPException(status_code=400, detail="There was an error while generating your Data'.")
            
    def Generate_data(self, topic: str,number_records:int):
 
    # Define the mapping of the format of the prompt to the function that will generate the prompt.

        output_parser = JsonOutputParser(pydantic_object=LangChainSchema)
        preview_prompt = PromptTemplate(template=main_template, input_variables=["topic",'number_records'],
                                        partial_variables={"prompt_format":output_parser.get_format_instructions()})
        previewed_data_chain = preview_prompt | azure_llm | output_parser 

        try:
            preview_prompt_response = previewed_data_chain.invoke({'topic': topic,"number_records":number_records})
            #preview_prompt_formated_response = preview_prompt_response.replace('\\n', '\n')
            print(preview_prompt_response)
            return preview_prompt_response
            # Convert the response to a JSON object
            #json_response = json.dumps(preview_prompt_formated_response)
            #print(json_response)
            #return json_response
            

        except HTTPException as e:
                raise HTTPException(status_code=400, detail="There was an error while generating your Data'.")
        
        

        