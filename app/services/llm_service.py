
from llm.llm_class import GenerateSyntheticData 
from config import azure_chat_llm
from llm import convert_schemas_service
import json 
class LLMGenerateService:


    def generate_data(self,topic: str, instructions: str, prefix: str, example: str, number_of_records: int,data_format :str):
        
        generate_synthetic_data = GenerateSyntheticData(azure_chat_llm)

        if data_format == 'LangChainSchema':
            json_file = generate_synthetic_data.generate_data(topic, instructions, prefix, example, number_of_records)
            return json_file
        elif data_format == 'ChatgptSchema':
            json_file = generate_synthetic_data.generate_data(topic, instructions, prefix, example, number_of_records)
            print("fahed")
            print(type(json.loads(json_file)))
            print("fahed")
            return self.convert_output(json.loads(json_file)['messages'], convert_schemas_service.generate_openai_record)       
        elif data_format == 'SharegptSchema':
            json_file = generate_synthetic_data.generate_data(topic, instructions, prefix, example, number_of_records)
            return self.convert_output(json.loads(json_file)['messages'], convert_schemas_service.generate_sharegpt_record) 
        elif data_format == 'custom':
            json_file = generate_synthetic_data.generate_custome_data(topic, instructions, prefix, example, number_of_records)
            return json_file
        

    def convert_output(self,items, function):
        records = []
        for item in items:
            record = function(item["SystemMessage"], item["HumanMessage"], item["AssistantMessage"])
            records.append(record)
        return records