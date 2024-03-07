from langchain.output_parsers import StructuredOutputParser, ResponseSchema

class OpenAIFormat(StructuredOutputParser):
    def __init__(self):
        response_schemas = [
            ResponseSchema(
                name="messages", 
                description="An array of question-answer pairs, each represented as a message.", 
                schema=[
                    {"name": "question", "type": "string", "description": "The question posed by the user."},
                    {"name": "answer", "type": "string", "description": "The chatbot's response to the question."}
                ]
            )
        ]
        super().__init__(response_schemas=response_schemas)

    def parse(self, llm_output: str):
        structured_output = super().parse(llm_output)

        qa_pairs_transformed = []
        for pair in structured_output['messages']:

            system_message = {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}
            user_message = {"role": "user", "content": pair['question']}
            assistant_message = {"role": "assistant", "content": pair['answer']}
            qa_pairs_transformed.append({"messages": [system_message, user_message, assistant_message]})

        return qa_pairs_transformed