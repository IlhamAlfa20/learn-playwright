from playwright.sync_api import sync_playwright

def test_login_tokopedia():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 1. Buka web
        page.goto("https://www.tokopedia.com")

        # 2. login
        page.wait_for_selector('div.css-11hzwo5', timeout=2000)
        page.click('div.css-11hzwo5')
        page.wait_for_timeout(1000)

        page.click('[data-testid="btnHeaderLogin"]')

        page.wait_for_timeout(5000)

        print("✅ Test selesai sukses!")

        browser.close()

if __name__ == "__main__":
    test_login_tokopedia()


