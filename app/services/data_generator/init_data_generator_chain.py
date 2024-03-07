from services.data_generator.data_generator_chain import DataGen
from fastapi import HTTPException


def generate_data_set(topic, format,number_of_records):     
    data_gen_obj = DataGen()
    if format == "langchain":
        response_langchain = data_gen_obj.genrate_langchain_format(topic, number_of_records)
        return response_langchain
    elif format == "gpt":
        response_gpt = data_gen_obj.generate_openai_format(topic, number_of_records)
        return response_gpt
        

    


