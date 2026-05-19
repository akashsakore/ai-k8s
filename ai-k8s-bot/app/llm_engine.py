from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_issue(logs, events, status):

    prompt = f"""
    You are a Kubernetes troubleshooting expert.

    Analyze:

    Status:
    {status}

    Events:
    {events}

    Logs:
    {logs}

    Give:
    1. Root cause
    2. Suggested fix
    3. Severity
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
