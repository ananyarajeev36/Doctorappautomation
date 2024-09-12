from functionalities import global_helper_function,adminlogin
from playwright.sync_api import sync_playwright, Page, expect
def test_addspecialization():
    page, browser, playwright = global_helper_function()
    try:
        a=adminlogin(page)
        page.locator('a.sidebar-link[href="#/specialization"]').click()
        page.wait_for_timeout(6000) 
        page.get_by_role("button",name=" Add").click()    
        page.locator(".modal-content").click()
        page.wait_for_timeout(1000) 
        page.fill('input[name="name"]', "Pulmanology")
        page.wait_for_timeout(4000) 
        page.get_by_role("button",name="Save").click()


        
        
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Specialization added successfully"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        
        
        page.wait_for_timeout(6000) 
        print("Specializationadded successfully")
        




    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_addspecializationerror1():
    page, browser, playwright = global_helper_function()
    try:
        a=adminlogin(page)
        page.locator('a.sidebar-link[href="#/specialization"]').click()
        page.wait_for_timeout(6000) 
        page.get_by_role("button",name=" Add").click()    
        page.locator(".modal-content").click()
        page.wait_for_timeout(1000) 
        page.fill('input[name="name"]', "")
        page.wait_for_timeout(4000) 
        page.get_by_role("button",name="Save").click()

        
        
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Specialization field cannot be empty"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        
        
        page.wait_for_timeout(6000) 
        print("The admin is able to view proper error response specifying about the specialization field cannot be empty")
        




    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()




    

if __name__ == "__main__":
    test_addspecialization()
    test_addspecializationerror1()
   
