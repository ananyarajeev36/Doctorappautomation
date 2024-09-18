# Source code for verifying the stored error message with the help of csv file.
from playwright.sync_api import sync_playwright, Page, Browser,expect
from functionalities import global_helper_function
import re
import csv
import pytest
def load_test_data():
    with open("testdata.csv") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]



    
@pytest.mark.parametrize("data", load_test_data())
def test_has_title_and_click_login(data):
    # Get the page, browser, and playwright from the global helper function
    page, browser, playwright = global_helper_function()
    username = data["username"]
    password = data["password"]
    expected=data["expected"]
    response_data = {}
    
    try:
        
        # Navigate to the page
        page.goto("http://34.93.203.11:8081")
        print("Check whether the user is able to launch the website.")
        expected_success_message="Login Successfull"
        page.get_by_role("button", name="Login").click()
        print("Check whether the doctor is able to perform login operation.")
        page.fill('input[name="username"]',username)
        page.fill('input[name="password"]',password)
        

        page.get_by_role("button", name="Login").click()
        toast_selector = "div.Toastify__toast-body"
        page.wait_for_selector(toast_selector, timeout=5000)
        
        # Locate the toast message
        toast = page.locator(toast_selector)
        
        # Here we compare the actual and expected error message from data take from the csv
        toast_text = toast.text_content().strip()
        if expected=="Invalid password, please try again.":
            assert toast_text == expected, f"Alert message mismatch! Expected: {expected}, Got: {toast_text}"
            print("Alert message is correct:", toast_text)
        elif expected=="Invalid Username or Password":
            assert toast_text == expected, f"Alert message mismatch! Expected: {expected}, Got: {toast_text}"
            print("Alert message is correct:", toast_text)
        
            

       
        page.wait_for_timeout(10000) 
       
        
        
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

if __name__ == "__main__":
    test_has_title_and_click_login()
  