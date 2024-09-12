from functionalities import global_helper_function, patientlogin

def test_bookslot():
    page, browser, playwright = global_helper_function()
    try:
        # Navigate to the page
        abc=patientlogin(page)
        page.locator('a.sidebar-link[href="#/slot-booking"]').click()
        page.wait_for_timeout(12000)
        button=page.locator("//html/body/div/div/div/div[2]/table/tbody/tr[2]/td[4]/button").click()
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        # Locate the toast message
        toast = page.locator(toast_selector)
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="Slot Booked"
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)
        print("The user is able to book the slot")
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_bookslot1():
    page, browser, playwright = global_helper_function()
    try:
        # Navigate to the page
        abc=patientlogin(page)
        page.locator('a.sidebar-link[href="#/slot-booking"]').click()
        page.wait_for_timeout(12000)
        button=page.locator("//html/body/div/div/div/div[2]/table/tbody/tr[1]/td[4]/button").click()
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        # Locate the toast message
        toast = page.locator(toast_selector)
        # Get the text content of the toast message
        toast_text = toast.text_content().strip()
        page.wait_for_timeout(6000) 
        # Expected toast message
        expected_toast_message ="You already have another appointment on the same date and time"
        # Validate the toast message
        assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
        page.wait_for_timeout(6000)
        print("The user is able to view proper error message specifying about the slot which is already booked")
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()        

if __name__ == "__main__":
    
    test_bookslot()
    test_bookslot1()
    