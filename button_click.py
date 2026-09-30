from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        page.goto(
            "https://bharathiraja2806.github.io/MyPortfolio/",
            wait_until="networkidle"
        )

        page.get_by_role("link", name="Skills").click()
        page.get_by_role("link", name="Contact", exact=True).click()

        input("Press Enter to close the browser...")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        browser.close()