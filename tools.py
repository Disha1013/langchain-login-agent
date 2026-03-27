from langchain_core.tools import tool
from playwright.sync_api import sync_playwright
import time
import threading

lock = threading.Lock()

browser = None
page = None
playwright_instance = None


def get_page():
    global browser, page, playwright_instance

    if page is None:
        print("🌐 Launching browser...")
        playwright_instance = sync_playwright().start()
        browser = playwright_instance.chromium.launch(headless=False)
        page = browser.new_page()

    return page


@tool
def go_to_url(url: str) -> str:
    """Navigate the browser to a given URL."""
    with lock:
        print(f"\n➡️ ACTION: Opening URL → {url}")
        get_page().goto(url)
        time.sleep(2)
        return f"Opened {url}"


@tool
def click_element(selector: str) -> str:
    """Click an element on the page using a CSS selector."""
    with lock:
        print(f"\n➡️ ACTION: Clicking → {selector}")
        get_page().click(selector)
        time.sleep(2)
        return f"Clicked {selector}"


@tool
def type_text(input: str) -> str:
    """
    Type text into an input field.

    Format: selector|text
    Example: #login_field|myusername
    """
    with lock:
        selector, text = input.split("|")

        print(f"\n➡️ ACTION: Typing into {selector}")
        print(f"   🔑 Value: {text}")

        get_page().fill(selector, text)
        time.sleep(1)

        return f"Typed into {selector}"


@tool
def get_page_text(_: str = "") -> str:
    """Get visible text content of the page."""
    with lock:
        print("\n📄 Reading page content...")
        return get_page().inner_text("body")[:2000]