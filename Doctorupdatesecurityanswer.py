from functionalities import global_helper_function,doctorlogin
from playwright.sync_api import sync_playwright, Page, expect

def test_updatesecurityanswer():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=doctorlogin(page)
        
        
        page.locator('a.sidebar-link[href="#/securityquestion"]').click()
        page.wait_for_timeout(2000) 
        page.fill('input[name="username"]', "Anand")
        page.get_by_role("button", name="Confirm").click() 
        page.wait_for_timeout(4000) 
        page.fill('input[name="security_answer"]', "Ananya")
        
        page.get_by_role("button", name="Save").click() 
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Security Answer updated successfully"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)
        print("The doctor is able to update the security answer")

            
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()
def test_updatesecurityanswrerror1():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=doctorlogin(page)
        page.locator('a.sidebar-link[href="#/securityquestion"]').click()
        page.fill('input[name="username"]', " ")
        page.get_by_role("button", name="Confirm").click() 
        
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Username does not match with the logged user"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)
        print("The user is able to view proper error message specifying about leaving mandatory field as empty")
            
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_updatesecurityanswer2():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=doctorlogin(page)
        
        page.locator('a.sidebar-link[href="#/securityquestion"]').click() 
        page.fill('input[name="username"]', "Anand")
        page.get_by_role("button", name="Confirm").click() 
        page.wait_for_timeout(3000) 
        page.evaluate("window.scrollBy(0, 1000)")
        page.fill('input[name="security_answer"]', "A")
        
        page.get_by_role("button", name="Save").click() 
        page.wait_for_timeout(3000)

          
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Ensure this field has at least 5 characters."
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)   
        print("The user is able to view proper error message specifying about the incorrect security answer")       
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_updatesecurityanswer3():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=doctorlogin(page)
        
        page.locator('a.sidebar-link[href="#/securityquestion"]').click()
        page.fill('input[name="username"]', "Anand")
        page.get_by_role("button", name="Confirm").click() 
        page.wait_for_timeout(3000)
        page.evaluate("window.scrollBy(0, 1000)") 
        page.fill('input[name="security_answer"]', "")
        
        page.get_by_role("button", name="Save").click() 
        page.wait_for_timeout(3000)

          
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="All fields are mandatory"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)   
        print("The user is able to view proper error message specifying about leaving the security answer as empty")       
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()


def test_updatesecurityanswer4():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=doctorlogin(page)
        
        page.locator('a.sidebar-link[href="#/securityquestion"]').click()
        page.fill('input[name="username"]', "wf")
        page.get_by_role("button", name="Confirm").click() 
        
       
        
        page.wait_for_timeout(3000)
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        
        expected_toast_message = "Username does not match with the logged user"
        
        # Validate the error message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)  
        print("The user is able to view proper error message specifying about leaving mandatory fields as empty.")     
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

if __name__ == "__main__":
      
     test_updatesecurityanswer()
     test_updatesecurityanswrerror1()
     test_updatesecurityanswer2()
     test_updatesecurityanswer3()
     test_updatesecurityanswer4()
           