from langchain_core.tools import tool
from playwright.sync_api import sync_playwright
import time

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
def open_url(url: str) -> str:
    """Open a URL in the browser."""
    print(f"\n ACTION: Opening URL → {url}")
    get_page().goto(url)
    time.sleep(2)
    return "Opened URL"

@tool
def type_username(username: str) -> str:
    """Type username into GitHub login field."""
    print(f"\n ACTION: Typing Username")
    get_page().fill("#login_field", username)
    time.sleep(1)
    return "Typed username"

@tool
def type_password(password: str) -> str:
    """Type password into GitHub password field."""
    print(f"\n ACTION: Typing Password")
    get_page().fill("#password", password)
    time.sleep(1)
    return "Typed password"

@tool
def click_login(_: str = "") -> str:
    """Click login button."""
    print(f"\n ACTION: Clicking Login")
    get_page().click("input[type='submit']")
    time.sleep(2)
    return "Clicked login"

@tool
def check_login_success(_: str = "") -> str:
    """Check if login was successful by looking for profile/avatar."""
    page = get_page()

    print("\n Checking login status...")

    try:
        page.wait_for_selector("img.avatar", timeout=5000)
        print(" Login successful!")
        return "Login successful"
    except:
        print(" Login might have failed")
        return "Login failed"