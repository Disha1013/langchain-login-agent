import os
from dotenv import load_dotenv
from agent import build_agent
from tools import check_login_success, open_url, type_username, type_password, click_login, check_login_success

load_dotenv()

USERNAME = os.getenv("GITHUB_USERNAME")
PASSWORD = os.getenv("GITHUB_PASSWORD")

agent = build_agent()

print("\n🤖 Starting Controlled Agent (SAFE)...\n")

# Read steps
with open("skill.md", "r") as f:
    steps = f.readlines()

for step in steps:
    step = step.strip()

    print(f"\n Step: {step}")

    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"""
You are an instruction parser.

Convert this step into a tool call.

Step:
{step}

Available tools:
- open_url(url)
- type_username(username)
- type_password(password)
- click_login()
- check_login_success()

IMPORTANT RULES:
- "Check if login was successful" → use check_login_success
- NEVER click login more than once
- DO NOT repeat previous actions

Return ONLY in this JSON format:
{{
  "tool": "tool_name",
  "input": "value"
}}

Use:
username = {USERNAME}
password = {PASSWORD}
"""
            }
        ]
    })

    output = response["messages"][-1].content
    print(" Agent Output:", output)

    if "open_url" in output:
        open_url.invoke("https://github.com/login")

    elif "type_username" in output:
        type_username.invoke(USERNAME)

    elif "type_password" in output:
        type_password.invoke(PASSWORD)

    elif "click_login" in output:
        click_login.invoke("")

    elif "check_login_success" in output:
        check_login_success.invoke("")

print("\n All steps completed safely!\n")