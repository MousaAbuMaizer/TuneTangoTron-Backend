import json
from datetime import datetime

def convertJsonToBytes(json_obj):
    json_str = json.dumps(json_obj)
    json_bytes = json_str.encode('utf-8')
    return json_bytes

def generate_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")