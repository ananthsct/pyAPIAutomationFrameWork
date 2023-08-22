# Help you to read the json files and provide you JSON data
import json


def get_payload_auth():
    # Read from auth.json and return json
    file_data = open("src/constants/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data


def common_headers():
    headers = {
        'Content-Type': 'application/json'
    }
    return headers


def common_put_patch_headers(booking_id):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": "token="+booking_id
    }
    return headers

# Read from the Excel and Run a Test case Multiple Times
# Data driven -

# Read data from Excel and Run the API - 100 Times
