import requests
import os
from dotenv import load_dotenv

load_dotenv()

def main(message):
    line_notify_token = os.environ['LINE_API_KEY']
    line_notify_api = os.environ['LINE_NOTIFY_URL']
    payload = {'message': '\n' + message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    try:        
        line_notify = requests.post(line_notify_api, data=payload, headers=headers)
        if line_notify.status_code == 200:
            print("success sent message")
    except Exception as e:
        print("line notify exception")
        print(e)
        pass
