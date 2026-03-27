import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from tools import open_url, type_username, type_password, click_login, check_login_success

load_dotenv()


def build_agent():
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",
        temperature=0
    )

    tools = [
        open_url,
        type_username,
        type_password,
        click_login,
        check_login_success
    ]

    agent = create_agent(
        model=llm,
        tools=tools
    )

    return agent