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
        page.wait_for_timeout(5000)  # Adjust timeout if necessary
        page.evaluate("window.scrollBy(0, 3000)")
        
        page.locator("//button[contains(text(), 'EDIT')]").first.click()
        page.wait_for_timeout(5000)
        page.locator('[name="profile_headline"]').fill("Athulya")
        page.locator("//input[@placeholder='Profile heading (Max 30 characters)']").fill("Athulya")
        
        page.locator("//input[@placeholder='Enter your full legal name']").fill("Athulya V Nair")
        
        page.locator("//input[@placeholder='Mention your stage name']").fill("Athuzzz")

        page.locator("//input[@placeholder='Provide weight']").fill(45)
        page.locator("//input[@placeholder='Provide height']").fill(145)
        page.locator('[name="number_of_movies"]').fill("12")
        page.locator('[name="number_of_television_roles"]').fill("12")
        page.locator('[name="number_of_theater_roles"]').fill("12")



        

        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_simple_login()
