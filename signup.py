
# from playwright.sync_api import sync_playwright, Page, Browser,expect
# from functionalities import global_helper_function




# # def test_has_title_and_click_login():
# #     # Get the page, browser, and playwright from the global helper function
# #     page, browser, playwright = global_helper_function()
    
# #     try:
# #         # Navigate to the page
# #         page.goto("http://34.93.203.11:8081")
# #         print("Check whether the user is able to launch the website.")
# #         # Expect a title "to contain" a substring "Doctor App"
# #         expect(page).to_have_title(re.compile("Doctor App"))
# #         print("Verify whether the page title is Doctor App.")
# #         # Locate the Login button by its text and click it
# #         page.get_by_role("button", name="Login").click()
# #         print("Check whether the doctor is able to perform login operation.")

# #         page.fill('input[name="username"]', "Anand")
# #         page.fill('input[name="password"]', "Ananya2006@")
# #         page.get_by_role("button", name="Login").click()
        
# #         page.wait_for_timeout(10000)  # Wait for 10 seconds
       
# #         # Logout functionality
# #         # page.goto("http://34.93.203.11:8081/#/")
# #         #  print("Check whether the user is able to perform logout operation.")
    
        
# #     finally:
# #         # Close the browser and Playwright
# #         browser.close()
# #         playwright.stop()

# # def test():
# #     # Get the page, browser, and playwright from the global helper function
# #     page, browser, playwright = global_helper_function()
    
# #     try:
# #         # Navigate to the page
# #         page.goto("http://34.93.203.11:8081")
# #         page.goto("http://34.93.203.11:8081/#/doctor-booked-slot")
# #         print("Check whether the user is able to launch the website.")
# #     finally:
# #         # Close the browser and Playwright
# #         browser.close()
# #         playwright.stop()


# # def testsignup():
   
# #     page, browser, playwright = global_helper_function()
    
# #     try:
# #         # Navigate to the page
# #         page.goto("http://34.93.203.11:8081")
       
# #         page.get_by_role("button", name="Register").click()
# #         print("Check whether the user is redirected to registration page")

# #         page.fill('input[name="username"]', "Anxgvab")
# #         page.fill('input[name="password"]', "Ananya2006@")
# #         page.fill('input[name="email"]', "ananyarb3@gmail.com")
# #         page.select_option("select#user_type", value="doctor")
# #         page.select_option("select#security_question", value="What is your pet's name?")
# #         page.fill('input[name="security_answer"]', "Ananya")
# #         print("Hellooo")
# #         page.get_by_role("button", name="Register").click()
        
# #         print("Hellooo")
# #         page.wait_for_timeout(10) 
     
       
# #     finally:
# #         # Close the browser and Playwright
# #         browser.close()
# #         playwright.stop()
# def testsignup():
#     page, browser, playwright = global_helper_function()
    
#     try:
#         # Navigate to the page
#         page.goto("http://34.93.203.11:8081")
       
       
#         # # Click on Register button
#         page.get_by_role("button", name="Register").click()
#         print("Check whether the user is redirected to registration page")
        
#         # # Fill the registration form
#         page.fill('input[name="username"]', "egkeut")
#         page.wait_for_timeout(1000)
#         page.fill('input[name="password"]', "Ananya2006@")
#         page.wait_for_timeout(1000)
#         page.fill('input[name="email"]', "hgfbeyqj@gmail.com")
#         page.wait_for_timeout(1000)
#         page.select_option("select#user_type", value="doctor")
#         page.wait_for_timeout(1000)
#         page.select_option("select#security_question", value="What is your pet's name?")
#         page.wait_for_timeout(1000)
#         page.fill('input[name="security_answer"]', "Ananya")
#         page.wait_for_timeout(1000)
        
#         # Submit the registration form
#         page.get_by_role("button", name="Register").click()
#         page.wait_for_selector("div.Toastify__toast-body", timeout=5000)  # Adjust the selector based on your HTML structure
        
#         # Locate the toast notification
#         toast = page.locator("div.Toastify__toast-body")
#         toast_text = toast.text_content().strip()
        
#         # Define the expected toast message
#         expected_toast_message = "User registered successfully"
        
#         # Validate the toast message
#         assert toast_text == expected_toast_message, f"Expected toast message '{expected_toast_message}', but got '{toast_text}'"
#         print("Toast message validation passed.")




        
#         # Wait for a response or error
#         page.wait_for_timeout(2000)  
        
#         print("Registration successful.")
#         page.wait_for_timeout(3000)
#         page.fill('input[name="username"]', "admin")
#         page.wait_for_timeout(2000)
#         page.fill('input[name="password"]', "Admin@123")
#         page.wait_for_timeout(2000)
#         page.get_by_role("button", name="Login").click()
#         page.wait_for_timeout(3000)
#             # page.goto("http://34.93.203.11:8081/#/pending-doctors").click()
#             # page.locator('a[href="#/pending-doctors"]').click()
#             # page.get_by_text(" PENDING DOCTORS").click()
#         page.locator('a.sidebar-link[href="#/pending-doctors"]').click()
        
#         page.wait_for_timeout(5000)
#             # Locate an element inside a specific row and column in the table
#         page.locator("//html/body/div/div/div/div[2]/table/tbody[1]/tr/td[3]/button").click()


#         page.wait_for_timeout(5000)  # Adjust waiting time as necessary

#     finally:
#         # Close the browser and Playwright
#         browser.close()
#         playwright.stop()


# # def testapprove():
# #     page, browser, playwright = global_helper_function()

# #     try:
# #         page.goto("http://34.93.203.11:8081/#/pending-doctors")    
# #     finally:
# #         # Close the browser and Playwright
# #         browser.close()
# #         playwright.stop()






# Code for performing sign up by taking values from the csv file
from playwright.sync_api import sync_playwright, Page, Browser,expect
from functionalities import global_helper_function


import csv
import pytest

def load_test_data():
    with open("signup.csv") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]



    
@pytest.mark.parametrize("data", load_test_data())
def testsignup1usingcsv(data):
    page, browser, playwright = global_helper_function()
    username = data["username"]
    password = data["password"]
    email=data["email"]
    user_type=data["user_type"]
    security_question=data["security_question"]
    security_answer=data["security_answer"]



    try:
        # Navigate to the page
        page.goto("http://34.93.203.11:8081")
       
        # Click on Register button
        page.get_by_role("button", name="Register").click()
        print("Check whether the user is redirected to registration page")
        
        
        
        # Fill the registration form
        page.fill('input[name="username"]', username)
        page.wait_for_timeout(3000)
        page.fill('input[name="password"]', password)
        page.fill('input[name="email"]', email)
        page.select_option("select#user_type",user_type)
        page.select_option("select#security_question",security_question)
        page.fill('input[name="security_answer"]',security_answer)
        page.get_by_role("button", name="Register").click()
        page.wait_for_timeout(5000) 

    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

if __name__ == "__main__":
    #  test_has_title_and_click_login()
    # testsignup()
    # testsignup1()
    testsignup1usingcsv()
