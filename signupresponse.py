# Source code for saving the response of signup id,email in json file with in the same directorary

from playwright.sync_api import sync_playwright, Page, Browser, expect
from functionalities import global_helper_function

import csv
import pytest
import json
import os

def load_test_data():
    file_path = "C:/Users/infolitz/nu/Doctorappautomation/signup.csv"  # Use absolute path
    with open(file_path) as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

# Function to write the user ID or response data to a file
def write_response_to_file(response_data, file_path="signup_response.json"):
    """Writes response data to a file."""
    with open(file_path, 'w') as file:
        json.dump(response_data, file, indent=4)
    print(f"Response data written to {file_path}")

# Parametrize the test with data from CSV
@pytest.mark.parametrize("data", load_test_data())
def testsignup1usingcsv(data):
    page, browser, playwright = global_helper_function()

    # Extracting values from CSV data
    username = data["username"]
    password = data["password"]
    email = data["email"]
    user_type = data["user_type"]
    security_question = data["security_question"]
    security_answer = data["security_answer"]

    # Define a variable to store response data
    response_data = {}

    # Define the response handler for network interception
    def handle_response(response):
        if "signup" in response.url and response.status == 201:
            try:
                # Extract the response JSON data
                response_body = response.json()
                # Extracting the user ID and email from the response
                user_id = response_body.get("data", {}).get("id")
                email = response_body.get("data", {}).get("email")
                user_type=response_body.get("data",{}).get("user_type")
                security_question=response_body.get("data",{}).get("security_question")
                security_answer=response_body.get("data",{}).get("security_answer")
                username=response_body.get("data",{}).get("username")                

                response_data['id'] = user_id
                response_data['email'] = email
                response_data['user_type']=user_type
                response_data['security_question']=security_question
                response_data['security_answer']=security_answer
                response_data['username']=username
                response_data['status'] = "success"
                response_data['message'] = response_body.get("message", "No message in response")
                print("Captured response data:", response_data)
            except Exception as e:
                print(f"Failed to parse response: {e}")

    try:
        # Print current working directory for debugging
        

        # Set up response interception for signup API call
        page.on("response", handle_response)

        # Navigate to the signup page
        page.goto("http://34.93.203.11:8081")

        # Click on Register button
        page.get_by_role("button", name="Register").click()
        print("Check whether the user is redirected to the registration page")

        # Fill the registration form
        page.fill('input[name="username"]', username)
        page.wait_for_timeout(3000)
        page.fill('input[name="password"]', password)
        page.fill('input[name="email"]', email)
        page.select_option("select#user_type", user_type)
        page.select_option("select#security_question", security_question)
        page.fill('input[name="security_answer"]', security_answer)
        page.get_by_role("button", name="Register").click()
        page.wait_for_timeout(5000)

        # Wait for network calls to finish and capture the response
        page.wait_for_load_state("networkidle")

    finally:
        # Write the captured response data to a file
        if response_data:
            write_response_to_file(response_data)
        else:
            print("No response data to write.")

        # Close the browser and Playwright
        browser.close()
        playwright.stop()

if __name__ == "__main__":
    pytest.main()
