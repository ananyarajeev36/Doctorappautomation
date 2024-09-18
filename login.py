# from playwright.sync_api import sync_playwright, Page, Browser,expect
# from functionalities import global_helper_function
# import re
# def test_has_title_and_click_login():
#     # Get the page, browser, and playwright from the global helper function
#     page, browser, playwright = global_helper_function()
    
#     try:
#         # Navigate to the page
#         page.goto("http://34.93.203.11:8081")
#         print("Check whether the user is able to launch the website.")
#         # Expect a title "to contain" a substring "Doctor App"
#         expect(page).to_have_title(re.compile("Doctor App"))
#         print("Verify whether the page title is Doctor App.")
#         # Locate the Login button by its text and click it
#         page.get_by_role("button", name="Login").click()
#         print("Check whether the doctor is able to perform login operation.")

#         page.fill('input[name="username"]', "Anand")
#         page.fill('input[name="password"]', "Ananya2006@")
#         page.get_by_role("button", name="Login").click()
        
#         page.wait_for_timeout(10000)  # Wait for 10 seconds
       
#         # Logout functionality
#         # page.goto("http://34.93.203.11:8081/#/")
#         #  print("Check whether the user is able to perform logout operation.")
    
        
#     finally:
#         # Close the browser and Playwright
#         browser.close()
#         playwright.stop()

# if __name__ == "__main__":
#     test_has_title_and_click_login()
  


# Source code for performing login by retriving data from the csv file.


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
    # errormessage=data["errormessage"]
    
    try:
        
        # Navigate to the page
        page.goto("http://34.93.203.11:8081")
        print("Check whether the user is able to launch the website.")
        
        page.get_by_role("button", name="Login").click()
        print("Check whether the doctor is able to perform login operation.")
        page.fill('input[name="username"]',username)
        page.fill('input[name="password"]',password)
        

        page.get_by_role("button", name="Login").click()
       
        page.wait_for_timeout(10000)  # Wait for 10 seconds
       
        # Logout functionality
        # page.goto("http://34.93.203.11:8081/#/")
        #  print("Check whether the user is able to perform logout operation.")
    
        
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

if __name__ == "__main__":
    test_has_title_and_click_login()
  