import os
import json
from Output_schemes import LangChainSchema, ChatgptSchema
from langchain_core.output_parsers import JsonOutputParser

def choose_output_parser(data_format):
    if data_format == 'LangChainSchema':
        output_parser=JsonOutputParser(pydantic_object=LangChainSchema)
        return output_parser
    elif data_format == 'ChatgptSchema':
        output_parser=JsonOutputParser(pydantic_object=ChatgptSchema)
        return output_parser
    

def save_output_to_json(output, folder_path='GeneratedData', file_name ='GeneratedData.json'):
    """
    Saves the given output to a JSON file inside the specified folder.

    Parameters:
    - output: The data to be saved in JSON format.
    - folder_path: The path of the folder where the JSON file will be saved.
    - file_name: The name of the JSON file.
    """
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Write the output to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(output, json_file, indent=4)
