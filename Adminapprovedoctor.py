from functionalities import global_helper_function,adminlogin
from playwright.sync_api import sync_playwright

def testadddoctor():
    page, browser, playwright = global_helper_function()
    try:
        abc=adminlogin(page)  
        
        page.wait_for_timeout(3000)  
        page.locator('a.sidebar-link[href="#/pending-doctors"]').click()
        page.wait_for_timeout(5000)
            # Locate an element inside a specific row and column in the table
            
        button=page.locator("//html/body/div/div/div/div[2]/table/tbody[1]/tr/td[3]/button").click()
            
        print("The admin is able to add the doctor.")

        page.wait_for_timeout(8000)  # Adjust waiting time as necessary
       
        
            
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

if __name__ == "__main__":
  
    testadddoctor()
