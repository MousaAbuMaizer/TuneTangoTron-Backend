from langchain.prompts import PromptTemplate
from llm_prompts import Generate_Data_prompt ,Sample_Data_prompt,Sample_Data_langchain_format,Sample_Data_openai_format,Generate_Data_openai_format,Generate_Data_langchain_format
from langchain_core.output_parsers import JsonOutputParser ,StrOutputParser
from fastapi import HTTPException
from __init__ import azure_llm
from Output_schemes import LangChainSchema , ChatgptSchema
from error_handling import handle_format_error
import json
from utils import save_output_to_json , choose_output_parser

            
class Prompt_Preview:
    """this function that takes input and generate 5 prompts based on a certain topic"""
    def Generate_example_data(self, topic: str,data_format):
            output_parser= choose_output_parser(data_format)

            Sample_Data_Template = PromptTemplate(template=Sample_Data_prompt, input_variables=["topic"],
                                            partial_variables={"prompt_format":output_parser.get_format_instructions()})
            Sample_Data_chain = Sample_Data_Template | azure_llm | output_parser 

            try:
                Sampled_Data = Sample_Data_chain.invoke({'topic': topic})
                print(Sampled_Data)
                return Sampled_Data
                

            except HTTPException as e:
                 raise HTTPException(status_code=400, detail="There was an error while generating your Data'.")
            
    '''this function will generate data based on topics and number of generated data the user wants '''   
    def Generate_data(self, topic: str,number_records:int ,data_format:str):
        #this if statement to chose the format of the prompt
        output_parser= choose_output_parser(data_format)

        Generate_Data_Template = PromptTemplate(template=Generate_Data_prompt, input_variables=["topic",'number_records'])
        Generated_Data_chain = Generate_Data_Template | azure_llm | output_parser 

        try:
            Generated_Data = Generated_Data_chain.invoke({'topic': topic,"number_records":number_records})
            print(Generated_Data)
            #this function will create folder and save the response on json format
            save_output_to_json(Generated_Data)
            print("saved")
            return Generated_Data
            

        except HTTPException as e:
                raise HTTPException(status_code=400, detail="There was an error while generating your Data'.")

class preview_prompts_v2:
    """this function that takes input and generate 5 prompts based on a certain topic"""

    def Generate_example_data_v2(self, topic: str , prompt_format:str) -> str:
            """
            Generate example data based on the provided topic.

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
        'LangChainSchema': Sample_Data_openai_format,
        'ChatgptSchema': Sample_Data_langchain_format
    }
            output_parser = StrOutputParser()
            handle_format_error(prompt_format, format_mapping)
            preview_prompt = PromptTemplate(template=format_mapping[prompt_format], input_variables=["topic"])
            previewed_data_chain = preview_prompt | azure_llm | output_parser

            try:
                preview_prompt_response = previewed_data_chain.invoke({'topic': topic})
                print(preview_prompt_response)
                return preview_prompt_response
                

            except HTTPException as e:
                 raise HTTPException(status_code=400, detail="There was an error while generating your Data'.")
        
    """this function will generate data based on topics and number of generated data the user wants """

    def Generate_data_v2(self, topic: str ,number_records:int,prompt_format:str) -> str:
            """
            Generate example data based on the provided topic.

            Parameters:
            - topic (str): The topic for which prompts will be generated.
            - number_records (int) : number of records to be generated.
            - prompt_format (str): The format of the prompt to be generated.

            Returns:
            - generated data(str):generated data based on the topic.

            Raises:
            - HTTPException: If there was an issue during prompt generation.
            """
            # Define the mapping of the format of the prompt to the function that will generate the prompt.
            format_mapping = {
        'ChatgptSchema': Generate_Data_openai_format,
        'LangChainSchema': Generate_Data_langchain_format
    }
            output_parser = StrOutputParser()
            handle_format_error(prompt_format, format_mapping)
            preview_prompt = PromptTemplate(template=format_mapping[prompt_format], input_variables=["topic","number_records"])
            previewed_data_chain = preview_prompt | azure_llm | output_parser

            try:
                preview_prompt_response = previewed_data_chain.invoke({'topic': topic, "number_records":number_records})
                preview_prompt_formated_response = preview_prompt_response.replace('\\n', '\n')
                 # Save Response To Json file
                save_output_to_json(preview_prompt_response)
                print(preview_prompt_response)
                print("saved")
                return preview_prompt_response
               
                

            except HTTPException as e:
                 raise HTTPException(status_code=400, detail="There was an error while generating your Data'.")
