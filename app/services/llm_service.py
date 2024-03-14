
from llm.llm_class import GenerateSyntheticData 

class LLMGenerateService:


    def generate_data(topic: str, instructions: str, prefix: str, example: str, number_of_records: int,data_format :str):

        if data_format == 'LangChainSchema':
            json_file = GenerateSyntheticData.generate_data(topic, instructions, prefix, example, number_of_records)
            return json_file
        elif data_format == 'ChatgptSchema':
            pass
