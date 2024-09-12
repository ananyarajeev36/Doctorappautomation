from functionalities import global_helper_function,doctorlogin
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
def test_createslot():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=doctorlogin(page)
       
        page.locator('a.sidebar-link[href="#/add-slots"]').click()
        page.wait_for_timeout(8000) 
        page.get_by_role("button", name=" Add").click() 
        page.locator(".modal-content").click()
        page.select_option("select#s2", value="Tuesday")
        page.wait_for_timeout(1000) 
        page.evaluate("document.querySelector('select#s2').blur()") 
            
        
           
        page.wait_for_timeout(1000) 
            
        page.locator("//input[@name='time']") .click()
        print("hello")
        page.fill('input[name="time"]', "12:08")
        page.wait_for_timeout(2000)
        print("Slot added successfully")
        page.get_by_role("button",name="SAVE").click() 
        page.wait_for_timeout(2000)

    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_deleteslot():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=doctorlogin(page)
       
        page.locator('a.sidebar-link[href="#/add-slots"]').click()
        page.wait_for_timeout(8000) 
        page.locator('xpath=//*[@id="root"]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[7]/button').click()
        print("Button clicked")   
        page.wait_for_timeout(3000)
        print("Deleted successfully")         
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()


def test_addsloterror1():
    page, browser, playwright = global_helper_function()
    try:
        a=doctorlogin(page)
        page.locator('a.sidebar-link[href="#/add-slots"]').click()
        page.wait_for_timeout(8000) 
        page.get_by_role("button", name=" Add").click() 
        
        page.get_by_role("button",name="SAVE").click() 
        page.wait_for_timeout(1000) 
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Please enter all fields"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000) 
        print("The doctor is able to view proper error message specifying about leaving mandatory field as empty")
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_addsloterror2():
    page, browser, playwright = global_helper_function()
    
    try:
        abc=doctorlogin(page)
       
        page.locator('a.sidebar-link[href="#/add-slots"]').click()
        page.wait_for_timeout(8000) 
        page.get_by_role("button", name=" Add").click() 
        page.locator(".modal-content").click()
        page.select_option("select#s2", value="Tuesday")
        page.wait_for_timeout(1000) 
        page.evaluate("document.querySelector('select#s2').blur()") 
            
        print("Dropdown option selected successfully")
           
        page.wait_for_timeout(1000) 
            
        page.locator("//input[@name='time']") .click()
        print("hello")
            
        page.fill('input[name="time"]', "12:48")
            
        page.get_by_role("button",name="SAVE").click() 
       
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        expected_toast_message ="Slot already exists"
        
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000) 
        print("The doctor is able to view proper error message specifying about the entered slot is already exists")
              
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()




    

if __name__ == "__main__":
   
    test_createslot()
    test_deleteslot()
    test_addsloterror1()
    test_addsloterror2()

   
