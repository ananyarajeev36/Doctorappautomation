from playwright.sync_api import sync_playwright, Page, Browser,expect




def global_helper_function() -> tuple[Page, Browser, sync_playwright]:
    """Set up the browser and return a Page instance."""
    playwright = sync_playwright().start()
    # Launch Microsoft Edge
    browser = playwright.chromium.launch(channel="msedge", headless=False)  # Ensure to use the correct channel
    page = browser.new_page()
    return page, browser, playwright
def adminlogin(page: Page):
    page.goto("http://34.93.203.11:8081/")
       

      
    page.get_by_role("button", name="Login").click()
    print("Check whether the admin is able to perform login operation.")
 
    page.wait_for_timeout(3000)
    page.fill('input[name="username"]', "admin")
    page.wait_for_timeout(1000)
    page.fill('input[name="password"]', "Admin@123")
    
    page.get_by_role("button", name="Login").click()
    
    # Wait for the login process to complete
    page.wait_for_timeout(3000)

def doctorlogin(page: Page):
    page.goto("http://34.93.203.11:8081/")
       
      
    page.get_by_role("button", name="Login").click()
    print("Check whether the doctor is able to perform login operation.")

    page.wait_for_timeout(3000)
    page.fill('input[name="username"]', "Anand")
    page.wait_for_timeout(1000)
    page.fill('input[name="password"]', "Ananya2006@")
    
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(8000)
    # Wait for the login process to complete
   
def forgotpasswordlaunch(page: Page):
     page.goto("http://34.93.203.11:8081/")
     page.wait_for_timeout(1000) 
       
     page.get_by_role("button", name="Login").click()
     page.wait_for_timeout(1000) 
     page.locator("p:text('Forgot Password?')").click()
     page.wait_for_timeout(8000)
    # Wait for the login process to complete
def patientlogin(page: Page):
    page.goto("http://34.93.203.11:8081/")
    page.get_by_role("button", name="Login").click()
    print("Check whether the doctor is able to perform login operation.")

    page.wait_for_timeout(3000)
    page.fill('input[name="username"]', "Ambadi")
    page.wait_for_timeout(1000)
    page.fill('input[name="password"]', "Ananya2006@")
    
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(8000)
    # Wait for the login process to complete    