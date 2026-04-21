from playwright.sync_api import sync_playwright

def verify(page):
    page.goto("http://localhost:8000/index.html")
    page.wait_for_timeout(500)

    # Intraday
    page.locator("#tradeType").select_option("INTRA")

    # 1080x1920
    page.locator("#sizeSelect").select_option("1080x1920")
    page.wait_for_timeout(500)
    page.screenshot(path="verification/verify_intra_1080x1920.png", full_page=True)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify(page)
        finally:
            browser.close()
