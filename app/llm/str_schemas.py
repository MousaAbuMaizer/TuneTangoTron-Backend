import json

def generate_sharegpt_record(system_message,human_message, assistant_message):

     return json.loads(
            """
                {
                    "system": "{system_message}",
                    "conversations": [
                        {
                            "from": "human",
                            "value": "{human_message}"
                        },
                        {
                            "from": "gpt",
                            "value": "{assistant_message}"
                        }
                    ]
                }
            """)


def generate_openai_record(system_message,human_message, assistant_message):

     return json.loads(
            """
                {
                    "system": "{system_message}",
                    "conversations": [
                        {
                            "from": "human",
                            "value": "{human_message}"
                        },
                        {
                            "from": "gpt",
                            "value": "{assistant_message}"
                        }
                    ]
                }
            """)