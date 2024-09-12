from functionalities import global_helper_function
from playwright.sync_api import sync_playwright, Page, expect

def profileupdate():
    with sync_playwright() as playwright:
        # Initialize the browser and page
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # Navigate to the page
            page.goto("http://34.93.203.11:8081/")
           
            # Click on Login button
            page.get_by_role("button", name="Login").click()
            print("Check whether the doctor is able to perform login operation.")

            # Fill the login form and submit
            page.fill('input[name="username"]',"Adewtunw")
            page.fill('input[name="password"]',"Ananya2006@")
            page.get_by_role("button", name="Login").click()  
            
            # Wait for a response or error
            page.wait_for_timeout(2000)  
            error_message = page.query_selector("div.error-message")  
            if error_message:
                print("Login Failed")
            else:
                print("Login successful")
                
                # Navigate to the profile page
                page.locator('a.sidebar-link[href="#/profile"]').click()
                page.wait_for_timeout(1000) 
                
                # Click on the Edit button to update profile
                page.get_by_role("button", name=" Edit").click()
                page.wait_for_timeout(2000)

                page.evaluate('''() => {
                    const modal = document.querySelector('.modal-content');  // Adjust the selector if needed
                     if (modal) {
                         modal.style.overflowY = 'auto';  // Enable vertical scroll
                         modal.style.maxHeight = '60vh';  // Restrict modal height to 80% of the viewport height
                     }
                 }''')


                # Ensure the form is visible
                form_locator = page.locator('form')
                form_locator.scroll_into_view_if_needed()
                
                # Fill the form fields
                page.fill('input[name="first_name"]', "Ananya")
                print("First name filled")
                page.wait_for_timeout(1000)

                page.fill('input[name="last_name"]', "Rajeev")
                print("Last name filled")
                page.wait_for_timeout(1000)

                page.fill('input[name="city"]', "Ernakulam")
                page.wait_for_timeout(1000)

                page.fill('input[name="state"]', "Kerala")
                page.wait_for_timeout(1000)

                page.fill('input[name="pincode"]', "123476")
                page.wait_for_timeout(1000)

                 # # Manually scroll the modal to bring dropdown into view using JavaScript
                page.evaluate('''() => {
                     const modal = document.querySelector('.modal-content');  // Adjust the selector if needed
                     modal.scrollTop = modal.scrollHeight;
                 }''')
                page.wait_for_timeout(2000)  # Give time for the scroll to complete
                print("gfschg")
                page.wait_for_timeout(2000)  # Give time for the scroll to complete
                print("hello")   
                # # Wait for the specialization dropdown to appear
                # page.select_option("select#user_type", value="doctor")
            
           
                # Select an option
                page.select_option("select#specialization", value="ENT")
                page.wait_for_timeout(1000)
                print("Specialization")
                # Repeat for the second dropdown
                page.wait_for_timeout(1000)
                page.select_option("select#working_at", value="Renai Medicity")
                dropdown_locator = page.locator('select#working_at')
                page.wait_for_timeout(1000)
                print("hey")
                # page.wait_for_selector('select#working_at', state='attached', timeout=60000)
                dropdown_locator.scroll_into_view_if_needed(timeout=60000)
                dropdown_locator.click()
                page.wait_for_timeout(1000)  # Ensure dropdown options are visible

                

                # Uncomment this when ready to save changes
                page.get_by_role("button", name="Save Changes").click()
                page.wait_for_timeout(1000)  
                # page.get_by_role("button", name=" Back").click()

        finally:
            # Close the browser and Playwright
            browser.close()

if __name__ == "__main__":
    profileupdate()
