import os
import json
from dotenv import load_dotenv
from jira import JIRA

load_dotenv()

jira = JIRA(
    server=os.getenv("JIRA_URL"),
    basic_auth=(
        os.getenv("JIRA_EMAIL"),
        os.getenv("JIRA_API_TOKEN")
    )
)

with open("output/action_items.json", "r") as f:
    data = json.load(f)

for item in data["action_items"]:

    issue_dict = {
        "project": {"key": os.getenv("JIRA_PROJECT_KEY")},
        "summary": item["task"],
        "description": f"""
Owner: {item['owner']}
Deadline: {item['deadline']}
Generated from meeting transcript.
""",
        "issuetype": {"name": "Task"},
    }

    issue = jira.create_issue(fields=issue_dict)

    print(f"Created: {issue.key}")