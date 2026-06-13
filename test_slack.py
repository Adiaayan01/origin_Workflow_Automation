import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SLACK_WEBHOOK_URL")

payload = {
    "text": "✅ Slack integration working!"
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.text)