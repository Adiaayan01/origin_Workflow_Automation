import os

print("Starting workflow...")

os.system("python extractor.py")
os.system("python jira_integration.py")
os.system("python slack.py")

print("Workflow completed!")