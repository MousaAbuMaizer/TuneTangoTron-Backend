from langchain.chains import LLMChain
from services.data_generator.data_generator_prompt import data_gen_template
from output_schemes.langchain_scheme import LangChainSchema
from output_schemes.openai_scheme import OpenAIFormat
from langchain.output_parsers import PydanticOutputParser, StructuredOutputParser
from config import azure_llm
from langchain.prompts import PromptTemplate
from fastapi import HTTPException

class DataGen:
    def genrate_langchain_format(self, topic: str, number_of_records: int):
      langchain_parser = PydanticOutputParser(pydantic_object=LangChainSchema)
      data_gen_prompt = PromptTemplate(template= data_gen_template, input_variables=["topic", "number_of_records"], partial_variables={"format_instructions": langchain_parser.get_format_instructions()})
      
      default_data_format_chain = LLMChain(llm=azure_llm, prompt= data_gen_prompt, output_parser=langchain_parser, verbose=True)
      try:
        res = default_data_format_chain.invoke({"topic": topic, "number_of_records": number_of_records})
        return res
      except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def generate_openai_format(self, topic: str, number_of_records: int):
        openai_parser = OpenAIFormat()
        data_gen_prompt = PromptTemplate(template= data_gen_template, input_variables=["topic", "number_of_records"])
        
        openai_format_chain = LLMChain(llm= azure_llm, prompt=data_gen_prompt, output_parser= openai_parser, verbose= True)
        
        try:
            res =openai_format_chain.invoke({"topic": topic, "number_of_records": number_of_records})
            return res
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        
        
        
        

        
        

           
    
    