from playwright.sync_api import sync_playwright

# Define login details
URL = "https://thecastme.com/#/talent/login"
# expectedurl="https://thecastme.com/#/talent/login"
def test_simple_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True to run in headless mode
        page = browser.new_page()
        
        # Navigate to the login page                                        
        page.goto(URL)
        print("Opened the website.")
        page.wait_for_timeout(1000)
        # Click on the login button
       
        page.locator("//input[@placeholder='Email']").fill("athulya@gmail.com")
        page.wait_for_timeout(4000)
        page.locator("//input[@placeholder='Password']").fill("Ananya2006@")
       
        page.wait_for_timeout(5000)


        page.locator("//button[contains(text(), 'LOGIN')]").first.click()
        print("The user should be redirected to the login page.")
         # Adjust timeout if necessary
        page.wait_for_timeout(10000)
        page.get_by_text("Photos").click()
        page.wait_for_timeout(6000)
        page.evaluate("window.scrollBy(0, 8000)")
        page.locator('img[alt="Upload"]').click()
        print("hai")
        page.wait_for_timeout(10000)
        
        print("hai")




        

        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_simple_login()
