from functionalities import global_helper_function,forgotpasswordlaunch
import re
from playwright.sync_api import sync_playwright, Page, expect
def test_forgotpassword():
    page, browser, playwright = global_helper_function()
    
    try:
        # Navigate to the page
        abc=forgotpasswordlaunch(page)
        
        page.wait_for_timeout(1000) 
        page.fill('input[name="username"]', "Anand")
        page.get_by_role("button", name="Enter").click() 
        page.wait_for_timeout(3000) 

        # Scrolling for a specific position down
        page.evaluate("window.scrollBy(0, 1000)")
        page.fill('input[name="security_answer"]', "Ananya")
        page.fill('input[name="new_password"]', "Ananya2006@")
        page.get_by_role("button", name="Reset").click() 
       
       
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Password updated successfully"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)
        print("The user is able to view success message after changing the password")
        
            
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()
def test_forgotpassworderror1():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=forgotpasswordlaunch(page)
        page.fill('input[name="username"]', "")
        page.get_by_role("button", name="Enter").click() 
        page.wait_for_timeout(3000) 
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Invalid Username"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)
        print("The user is able to view proper error message specifying about leaving mandatory field as empty")
            
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_forgotpassword2():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=forgotpasswordlaunch(page)
        
        page.wait_for_timeout(1000) 
        page.fill('input[name="username"]', "Anand")
        page.get_by_role("button", name="Enter").click() 
        page.wait_for_timeout(3000) 
        page.evaluate("window.scrollBy(0, 1000)")
        page.fill('input[name="security_answer"]', "Csdffdsalifornia")
        page.fill('input[name="new_password"]', "Ananya2006@")
        page.get_by_role("button", name="Reset").click() 
        page.wait_for_timeout(3000)

          
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Incorrect security answer"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)   
        print("The user is able to view proper error message specifying about the incorrect security answer")       
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_forgotpassword3():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=forgotpasswordlaunch(page)
        
        page.wait_for_timeout(1000) 
        page.fill('input[name="username"]', "Anand")
        page.get_by_role("button", name="Enter").click() 
        page.wait_for_timeout(3000)
        page.evaluate("window.scrollBy(0, 1000)") 
        page.fill('input[name="security_answer"]', "Ananya")
        page.fill('input[name="new_password"]', "2006@")
        page.get_by_role("button", name="Reset").click() 
        page.wait_for_timeout(3000)

          
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Password criteria not met"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)   
        print("The user is able to view proper error message specifying about the incorrect security answer")       
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_forgotpassword4():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=forgotpasswordlaunch(page)
        page.fill('input[name="username"]', "Anand")
        page.get_by_role("button", name="Enter").click() 
        
        page.wait_for_timeout(3000) 
        page.evaluate("window.scrollBy(0, 1000)")
        page.fill('input[name="security_answer"]', "Ananya")
        page.fill('input[name="new_password"]', "2006@")
        
        page.wait_for_timeout(3000)
        error_message = page.locator('p.text-danger')  # Adjust the selector based on your HTML
        error_text = error_message.text_content().strip()  # Retrieve and clean the text content
        
        # Define the expected error message
        expected_error_message = "Atleast 1 uppercase, 1 lowercase, 1 number and 1 special character, length should be 6-15"
        
        # Validate the error message
        assert error_text == expected_error_message, f"Expected error message '{expected_error_message}', but got '{error_text}'"
        print("The user is able to view proper error message specifying abput the invalid password")
                
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_forgotpassword5():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=forgotpasswordlaunch(page)
        
        page.wait_for_timeout(1000) 
        page.fill('input[name="username"]', "Anand")
        page.get_by_role("button", name="Enter").click() 
        page.wait_for_timeout(3000) 
        page.evaluate("window.scrollBy(0, 1000)")
        page.fill('input[name="security_answer"]', "")
        page.fill('input[name="new_password"]', "")
        page.get_by_role("button", name="Reset").click() 
        
        page.wait_for_timeout(3000)
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        
        expected_toast_message = "All fields are mandatory"
        
        # Validate the error message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)  
        print("The user is able to view proper error message specifying about leaving mandatory fields as empty.")     
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()



if __name__ == "__main__":
   
    test_forgotpassword()
    test_forgotpassworderror1()
    test_forgotpassword2()
    test_forgotpassword3()
    test_forgotpassword4()
    test_forgotpassword5()
    