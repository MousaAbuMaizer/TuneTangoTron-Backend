def generate_sharegpt_record(system_message, human_message, assistant_message):
    record = {
        "system": system_message,
        "conversations": [
            {"from": "human", "value": human_message},
            {"from": "gpt", "value": assistant_message}
        ]
    }

    return record

def generate_openai_record(system_message, human_message, assistant_message):
    record = {
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": human_message},
            {"role": "assistant", "content": assistant_message}
        ]
    }
    return record


