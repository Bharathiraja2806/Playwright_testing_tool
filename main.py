from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://bharathiraja2806.github.io/MyPortfolio/")

    print(page.title())

    page.screenshot(path="screenshot.png")

    browser.close()