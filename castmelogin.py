from castmecommonplaywright import global_helper_function


# Define constants
URL = "https://thecastme.com/#/"
EXPECTED_URL = "https://thecastme.com/#/talent/view-profile"

def test_login():
    page, browser, playwright = global_helper_function()
    try:
        # Wait for any initial operations to complete
        page.goto(URL)
        print("Opened the website.")
        page.wait_for_timeout(5000)

        # Login process
        page.locator("//button[contains(text(), 'Login')]").first.click()
        page.wait_for_timeout(1000)
        page.locator("//input[@placeholder='Email']").fill("athulya@gmail.com")
        page.wait_for_timeout(1000)
        page.locator("//input[@placeholder='Password']").fill("Ananya2006@")
        page.wait_for_timeout(5000)
        page.locator("//button[contains(text(), 'LOGIN')]").first.click()
        print("Attempting login...")
        page.wait_for_timeout(5000)

        # URL Assertion
        actual_url = page.url
        assert actual_url == EXPECTED_URL, f"URL Mismatch! Expected: {EXPECTED_URL}, but got: {actual_url}"
        print("Login successful.")

        # Logout
        page.locator('img[alt="menu"]').click()
        page.wait_for_timeout(1000)
        page.locator('text="Logout"').click()
        page.wait_for_timeout(2000)
        browser.close()
    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()


def test_login_validation1():
    page, browser, playwright = global_helper_function()
    try:


        # Navigate to the website
        page.goto(URL)
        page.wait_for_timeout(2000)

        # Click login
        page.locator("//button[contains(text(), 'Login')]").first.click()
        page.wait_for_timeout(1000)

        # Leave email blank
        page.locator("//input[@placeholder='Email']").fill("")
        page.locator("//input[@placeholder='Password']").fill("Ananya2006@")
        page.wait_for_timeout(1000)
        page.locator("//button[contains(text(), 'LOGIN')]").first.click()
        page.wait_for_timeout(2000)

        # Check for validation message
        error_text = page.locator('span.text-red-500').inner_text()
        assert error_text == "Email required", f"Expected 'Email required' but got '{error_text}'"
        print("Validation message verified when the user leave the email as empty.")

    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()


def test_login_validation2():
    page, browser, playwright = global_helper_function()
    try:
        # Navigate to the website
        page.goto(URL)
        page.wait_for_timeout(2000)

        # Click login
        page.locator("//button[contains(text(), 'Login')]").first.click()
        page.wait_for_timeout(1000)

        # Leave email blank
        page.locator("//input[@placeholder='Email']").fill("athulya@gmail.com")
        page.locator("//input[@placeholder='Password']").fill("")
        page.wait_for_timeout(1000)
        page.locator("//button[contains(text(), 'LOGIN')]").first.click()
        page.wait_for_timeout(2000)

        # Check for validation message
        error_text = page.locator('span.text-red-500').inner_text()
        assert error_text == "Password required", f"Expected 'Password required' but got '{error_text}'"
        print("Validation message verified when the user leave the password field as empty.")

    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_login_validation3():
    page, browser, playwright = global_helper_function()
    try:

        # Navigate to the website
        page.goto(URL)
        page.wait_for_timeout(2000)

        # Click login
        page.locator("//button[contains(text(), 'Login')]").first.click()
        page.wait_for_timeout(1000)

        # Leave email blank
        page.locator("//input[@placeholder='Email']").fill("athulya@gmail.com")
        page.locator("//input[@placeholder='Password']").fill("Ananyaa2006@")
        page.wait_for_timeout(1000)
        page.locator("//button[contains(text(), 'LOGIN')]").first.click()
        page.wait_for_timeout(2000)

        # Check for validation message
        error_text = page.locator('div.text-red-500').inner_text()
        assert error_text == "No active account found with the given credentials", f"Expected 'No active account found with the given credentials' but got '{error_text}'"
        print("Validation message verified if the user entered password is invalid.")

    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

def test_login_validation4():
    page, browser, playwright = global_helper_function()
    try:

        # Navigate to the website
        page.goto(URL)
        page.wait_for_timeout(2000)

        # Click login
        page.locator("//button[contains(text(), 'Login')]").first.click()
        page.wait_for_timeout(1000)

        # Leave email blank
        page.locator("//input[@placeholder='Email']").fill("athuldya@gmail.com")
        page.locator("//input[@placeholder='Password']").fill("Ananya2006@")
        page.wait_for_timeout(1000)
        page.locator("//button[contains(text(), 'LOGIN')]").first.click()
        page.wait_for_timeout(2000)

        # Check for validation message
        error_text = page.locator('div.text-red-500').inner_text()
        assert error_text == "No active account found with the given credentials", f"Expected 'No active account found with the given credentials' but got '{error_text}'"
        print("Validation message verified.If the user entered email is wrong")

    finally:
        # Close the browser and Playwright
        browser.close()
        playwright.stop()

if __name__ == "__main__":
    test_login()
    test_login_validation1()
    test_login_validation2()
    test_login_validation3()
    test_login_validation4()
