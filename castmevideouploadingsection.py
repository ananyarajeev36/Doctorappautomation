from playwright.sync_api import sync_playwright

# Define login details
URL = "https://thecastme.com/#/talent/login"
# expectedurl="https://thecastme.com/#/talent/login"
def test_videouploading():
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
        page.get_by_text("Videos").click()
        page.wait_for_timeout(6000)
        page.evaluate("window.scrollBy(0, 12000)")
        page.locator("img[alt='upload']").click()
        page.wait_for_timeout(8000)
        # Video uploading dialogoue
        page.locator("//input[@placeholder='Video heading  (Max 30 characters)']").fill(" video")
        page.wait_for_timeout(6000)
        page.locator("xpath=/html/body/div[5]/div/div/div[2]/div/div[2]/div/span/div[2]/div/div/input").fill("https://youtu.be/xfjB8vz7HYk?si=zVyoRhH94yn_SbL0")
        print("hai")
        # Section for uploading the path of the actual thumbnail image.
        file_path = "C://Users//infolitz//Desktop//1.png"
        print("Thumbnail image")
    # Set file on hidden input (bypassing the plus button)
        page.set_input_files("input[type='file']", file_path)
        # For clicking the modal
        modal_selector=page.wait_for_selector("div.relative.bg-white.rounded-lg.shadow-lg.w-\\[90\\%\\].max-w-3xl.overflow-hidden")

        page.wait_for_timeout(2000)
        print("hey")
        # For selecting the save button which is displayed inside a modal.
        page.locator("button.px-4.py-2.font-semibold.rounded-lg.text-black.border-2.border-black").click()

        page.wait_for_timeout(5000)
        print("hello")
        page.get_by_role("button", name="Save").click()
        page.wait_for_timeout(5000)
        
   # Close the browser
        browser.close()

if __name__ == "__main__":
    test_videouploading()
