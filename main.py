import os
from dotenv import load_dotenv
from tools import go_to_url, type_text, click_element

load_dotenv()

USERNAME = os.getenv("GITHUB_USERNAME")
PASSWORD = os.getenv("GITHUB_PASSWORD")

print("\n🤖 Starting GitHub Login Agent...\n")

# Step 1: Open login page
go_to_url.invoke("https://github.com/login")

# Step 2: Type username
type_text.invoke(f"#login_field|{USERNAME}")

# Step 3: Type password
type_text.invoke(f"#password|{PASSWORD}")

# Step 4: Click login
click_element.invoke("input[type='submit']")

print("\n✅ Login flow completed\n")