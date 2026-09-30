from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    try:
        page = browser.new_page()

        page.goto("https://bharathiraja2806.github.io/MyPortfolio/")
    except Exception as e:
        print(f"page not found {e}")

    page.get_by_role("link", name="Skills").click()

    input("Press Enter to close the browser...")

    browser.close()