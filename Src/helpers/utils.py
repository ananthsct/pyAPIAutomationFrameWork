# Help you to read the json files and provide you JSON data
import json


def get_payload_auth():
    # Read from auth.json and return json
    file_data = open("Src/Constants/auth.json")
    data = json.loads(file_data)
    return data
