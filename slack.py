import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

webhook_url = os.getenv("SLACK_WEBHOOK_URL")

with open("output/action_items.json", "r") as f:
    data = json.load(f)

message = "📋 *Meeting Summary*\n\n"

message += "*Decisions:*\n"
for decision in data["decisions"]:
    message += f"• {decision}\n"

message += "\n*Action Items:*\n"
for item in data["action_items"]:
    message += (
        f"• {item['task']}\n"
        f"   Owner: {item['owner']}\n"
        f"   Deadline: {item['deadline']}\n\n"
    )

payload = {
    "text": message
}

response = requests.post(
    webhook_url,
    json=payload
)

if response.status_code == 200:
    print("✅ Slack summary sent successfully!")
else:
    print(f"❌ Error: {response.text}")