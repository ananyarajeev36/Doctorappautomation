from playwright.sync_api import sync_playwright

# Define login details
URL = "https://thecastme.com/#/"
expectedurl="https://thecastme.com/#/talent/view-profile"
def test_simple_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True to run in headless mode
        page = browser.new_page()
        
        # Navigate to the login page
        page.goto(URL)
        print("Opened the website.")
        page.wait_for_timeout(5000)
        # Click on the login button
        page.locator("//button[contains(text(), 'Login')]").first.click()
        page.wait_for_timeout(1000)
        page.locator("//input[@placeholder='Email']").fill("athulya@gmail.com")
        page.wait_for_timeout(1000)
        page.locator("//input[@placeholder='Password']").fill("Ananya2006@")
        page.wait_for_timeout(5000)
        # Click login button

        page.locator("//button[contains(text(), 'LOGIN')]").first.click()
        print("The user should be redirected to the login page.")
        page.wait_for_timeout(5000)  # Adjust timeout if necessary
        
        actual_url = page.url
        assert actual_url == expectedurl, f"URL Mismatch! Expected: {expectedurl}, but got: {actual_url}"
        page.wait_for_timeout(5000)
        page.get_by_role("img", name="menu").click()
        print("ck")

 
       
        
        
        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_simple_login()
