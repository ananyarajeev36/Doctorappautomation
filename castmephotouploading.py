from playwright.sync_api import sync_playwright

# Define login details
URL = "https://thecastme.com/#/talent/login"
# expectedurl="https://thecastme.com/#/talent/login"
def test_photouploading():
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
        page.wait_for_timeout(6000)
        # page.locator("xpath=/html/body/div[5]/div/div/div[2]/div/div[2]/label/img").click()
        # page.locator('img[alt="Upload"]').click()
        print("hai")
        file_path = "C://Users//infolitz//Desktop//1.png"
        print("Annaya")
    # Set file on hidden input (bypassing the plus button)
        page.set_input_files("input[type='file']", file_path)
        print("Annaya")
        page.wait_for_timeout(4000)
        # page.locator("//button[contains(text(), 'Save')]").click()
        page.get_by_role("button", name="Save").click()
        print("hey")
   # Close the browser
        browser.close()

if __name__ == "__main__":
    test_photouploading()
