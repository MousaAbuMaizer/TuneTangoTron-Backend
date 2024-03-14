
from llm.llm_class import GenerateSyntheticData 
from config import azure_chat_llm

class LLMGenerateService:


    def generate_data(self,topic: str, instructions: str, prefix: str, example: str, number_of_records: int,data_format :str):

        if data_format == 'LangChainSchema':
            generate_synthetic_data = GenerateSyntheticData(azure_chat_llm)
            json_file = generate_synthetic_data.generate_data(topic, instructions, prefix, example, number_of_records)
            return json_file
        elif data_format == 'ChatgptSchema':
            pass       
        elif data_format == 'SharegptSchema':
            pass
        elif data_format == 'custom':
            pass