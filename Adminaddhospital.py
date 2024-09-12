from playwright.sync_api import sync_playwright, Page, Browser,expect
from functionalities import global_helper_function,adminlogin
def test_addhospital():
    page, browser, playwright = global_helper_function()
    try:
        # Wait for any initial operations to complete
        page.wait_for_timeout(2000)
        a = adminlogin(page)
        # Check whether the admin is able to add hospital
        # Navigate to the hospital creation page
        page.locator('a.sidebar-link[href="#/hospital"]').click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Add").click()   
        page.wait_for_timeout(1000) 
        page.locator(".modal-content").click()
        page.wait_for_timeout(1000) 



        # Fill in the hospital form
        page.fill('input[name="name"]', "Ananya")
        page.wait_for_timeout(1000) 
        page.fill('input[name="city"]', "Kollam")
        page.wait_for_timeout(1000) 
        page.fill('input[name="state"]', "Kerala")
        page.wait_for_timeout(1000) 
        page.fill('input[name="pincode"]', "639523")
        page.wait_for_timeout(1000) 

        # Click the Save button
        page.get_by_role("button", name="Save").click()
        

        # Adjusted selector for the toast message
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        
        # Expected toast message
        expected_toast_message = "Hospital added successfully"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, "Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        print("Hospital added successfully")
        
        page.wait_for_timeout(6000) 
        print("The admin is able to view the added hospital")
        page.wait_for_timeout(4000) 
    
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()



def test_addhospitalerror1():
    page, browser, playwright = global_helper_function()
    try:
        # Perform the admin login operation
        adminlogin(page)
        
        page.wait_for_timeout(6000)  # Wait for the login process to complete
        
        # Navigate to the hospital creation page
        page.locator('a.sidebar-link[href="#/hospital"]').click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Add").click()
        page.wait_for_timeout(1000)
        page.locator(".modal-content").click()
        
        # Fill in the hospital form
        hospitalname="Renai Medicity"
        page.fill('input[name="name"]', "Renai Medicity")
        page.wait_for_timeout(1000)
        city="Ernakulam"
        page.fill('input[name="city"]', "Ernakulam")
        page.wait_for_timeout(1000)
        page.fill('input[name="state"]', "Kerala")
        page.wait_for_timeout(1000)
        page.fill('input[name="pincode"]', "639523")
     

   
        page.get_by_role("button", name="Save").click()
        
       
        page.wait_for_selector("div.Toastify__toast-body", timeout=5000)
        
        
        toast = page.locator("div.Toastify__toast-body")
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        
        # Expected error message
        # f is the string format literal used to provide hospital name as input to an error message.

        expected_toast_message = f"{hospitalname} already exists in {city}"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message'{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(8000)
        print("The admin is able to view proper error message specifying about the hospital is already exist in the system")
        
    
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()
    
def test_addhospitalerror2():
    page, browser, playwright = global_helper_function()
    try:
        # Wait for any initial operations to complete
        page.wait_for_timeout(2000)  
        a = adminlogin(page)
        
        # Navigate to the hospital creation page
        page.locator('a.sidebar-link[href="#/hospital"]').click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Add").click()   
        page.wait_for_timeout(1000) 
        page.locator(".modal-content").click()
        page.wait_for_timeout(1000) 

        # Fill in the hospital form with empty values
        page.fill('input[name="name"]', "")
        page.wait_for_timeout(1000) 
        page.fill('input[name="city"]', "")
        page.wait_for_timeout(1000) 
        page.fill('input[name="state"]', "")
        page.wait_for_timeout(1000) 
        page.fill('input[name="pincode"]', "")
        page.wait_for_timeout(1000) 

        # Click the Save button
        page.get_by_role("button", name="Save").click()
        
        # Adjusted selector for the toast message
        toast_selector = "div.Toastify__toast.Toastify__toast-theme--light.Toastify__toast--warning.Toastify__toast--close-on-click"
        
        # Wait for the toast message to appear
        page.wait_for_selector(toast_selector, timeout=10000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        actual_toast_text = toast.text_content().strip()
        
        # Expected toast message
        expected_toast_message = "All fields are mandatory"
        
        # Validate the toast message
        assert actual_toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{actual_toast_text}'"
        
        
        page.wait_for_timeout(6000) 
        print("The admin is able to view the error  message specifying about leaving mandatory fields as empty")
        page.wait_for_timeout(4000) 
    
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()


if __name__ == "__main__":

    test_addhospital()
    test_addhospitalerror1()
    test_addhospitalerror2()
 