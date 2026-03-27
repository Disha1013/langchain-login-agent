import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_groq import ChatGroq

from tools import go_to_url, click_element, type_text, get_page_text

load_dotenv()


def build_agent():
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",   
        temperature=0
    )

    tools = [
        go_to_url,
        click_element,
        type_text,
        get_page_text
    ]

    agent = create_agent(
        model=llm,
        tools=tools
    )

    return agent