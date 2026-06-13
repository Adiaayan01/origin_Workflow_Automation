import os
import json
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Read transcript
with open("transcript/meeting.txt", "r") as f:
    transcript = f.read()

prompt = f"""
Analyze this meeting transcript and return ONLY valid JSON.

Format:

{{
  "decisions": [],
  "action_items": [
    {{
      "task": "",
      "owner": "",
      "deadline": ""
    }}
  ]
}}

Rules:
- Extract decisions.
- Extract action items.
- If owner missing use "Unassigned".
- If deadline missing use null.
- Return JSON only.

Transcript:

{transcript}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

result = response.text.strip()

# Remove markdown if present
result = result.replace("```json", "")
result = result.replace("```", "").strip()

# Validate JSON
parsed = json.loads(result)

with open("output/action_items.json", "w") as f:
    json.dump(parsed, f, indent=4)

print("✅ Extraction completed")
print("✅ Saved to output/action_items.json")