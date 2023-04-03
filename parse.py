import json

def parse_message_payload(payload_data):
    tmp_dict = json.loads(payload_data)
    return tmp_dict