from langchain.prompts import PromptTemplate
from llm_prompts import Generate_Data_prompt ,Sample_Data_prompt
from langchain_core.output_parsers import JsonOutputParser ,StrOutputParser
from fastapi import HTTPException
from __init__ import azure_llm
from Output_schemes import LangChainSchema , ChatgptSchema
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
            
    #this function will generate data based on topics and number of generated data the user wants     
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
        