from castmecommonplaywright import global_helper_function

# Define login details
URL = "https://thecastme.com/#/talent/sign-up"
expectedurl="https://thecastme.com/#/talent/sign-up"

def test_signup():
    page, browser, playwright = global_helper_function()
    try:
        # Wait for any initial operations to complete
        page.goto(URL)
        print("Opened the website.")
        page.wait_for_timeout(1000)
        # Click on the login button
        page.locator("//button[contains(text(), 'Sign up')]")
        page.wait_for_timeout(1000)
        page.locator("//input[@placeholder='Email']").fill("vijay1@gmail.com")
        page.wait_for_timeout(4000)
        page.locator("//input[@placeholder='Password']").fill("Ananya2006@")
        page.locator("//input[@placeholder='Full Name']").fill("Ananya")
       
        page.get_by_role("button",name="SUBMIT").click()
       
        print("The user should be redirected to the login page.")
        page.wait_for_timeout(5000)  # Adjust timeout if necessary
        
        actual_url = page.url
        assert actual_url == expectedurl, f"URL Mismatch! Expected: {expectedurl}, but got: {actual_url}"
        page.wait_for_timeout(5000)

     
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()



if __name__ == "__main__":
    test_signup()
