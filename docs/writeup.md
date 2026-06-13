We first get the meeting transcript using a free online transcription tool and save it in the meeting.txt file.

main.py runs 3 files one by one.
1. extractor.py
2. jira_integration.py
3. slack.py

The extractor.py script reads the transcript and sends it to Gemini, which extracts action items, deadlines, decisions, and other important details from the meeting.

The extracted information is then structured into a JSON format. In jira_integration.py, this JSON data is sent to the Jira API to automatically create Jira tickets for each action item.

Finally, slack.py uses the Slack API to send a meeting summary containing the key decisions and action items to a Slack channel.

Assumptions:
1. Participants and action items are mentioned clearly enough for Gemini to identify task owners and deadlines.
2. The names are present in the transcript here, but actually there should be some mapping that "speaker 1" is Aditya, etc.

Improvements:
1. We can ask gemini to return the confidence score for each action item so that low confidence action items can also be set for manual check.
2. I would want a fine tuned model which is also trained on the previous transcripts for better results.