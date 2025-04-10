from playwright.sync_api import sync_playwright

# Define login details
URL = "https://thecastme.com/#/talent/login"
# expectedurl="https://thecastme.com/#/talent/login"
def test_simple_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True to run in headless mode
        page = browser.new_page()
        
        # Navigate to the login page                                        
        page.goto(URL)
        print("Opened the website.")
        page.wait_for_timeout(1000)
        # Click on the login button
       
        page.locator("//input[@placeholder='Email']").fill("athulya@gmail.com")
        page.wait_for_timeout(4000)
        page.locator("//input[@placeholder='Password']").fill("Ananya2006@")
       
        page.wait_for_timeout(5000)


        page.locator("//button[contains(text(), 'LOGIN')]").first.click()
        print("The user should be redirected to the login page.")
        page.wait_for_timeout(5000)  # Adjust timeout if necessary
        page.evaluate("window.scrollBy(0, 3000)")
        
        page.locator("//button[contains(text(), 'EDIT')]").first.click()
        page.wait_for_timeout(5000)
        
        page.locator('[name="profile_headline"]').fill("Athulya")
        page.wait_for_timeout(1000)
        page.locator("//input[@placeholder='Profile heading (Max 30 characters)']").fill("Athulya")
        page.wait_for_timeout(1000)
        page.locator("//input[@placeholder='Enter your full legal name']").fill("Athulya V Nair")
        page.wait_for_timeout(1000)
        page.locator("//input[@placeholder='Mention your stage name']").fill("Athuzzz")
        page.wait_for_timeout(2000)
        page.select_option('select[name="gender"]', value="Male")
        
        

        page.select_option('select[name="nationality"]', value="Aland Islands")
        page.select_option('select[name="common_ethnic_backgrounds"]', value="African")
        

        page.wait_for_timeout(5000)
        page.locator("//input[@placeholder='Provide weight']").fill("45")
        page.select_option('select[name="weight_unit"]', value="Kilograms")
        page.wait_for_timeout(1000)
        page.locator("//input[@placeholder='Provide height']").fill("145")
        page.select_option('select[name="height_unit"]', value="Inches")
        page.wait_for_timeout(1000)
        page.select_option('select[name="common_face_shapes"]', value="Round")

        page.wait_for_timeout(1000)
        page.select_option('select[name="common_nose_shapes"]', value="Greek Nose (Straight Nose)")
        page.wait_for_timeout(1000)
        page.select_option('select[name="common_chin_shapes"]', value="Protruding Chin")
        page.wait_for_timeout(1000)
        page.select_option('select[name="common_skin_tone_types"]', value="Fair")
        page.wait_for_timeout(1000)
        page.select_option('select[name="common_mouth_shapes"]', value="Heart-Shaped Lips")
        page.wait_for_timeout(1000)
        page.select_option('select[name="common_hair_colors"]', value="Brown")
        page.wait_for_timeout(1000)
        page.select_option('select[name="common_lip_shapes"]', value="Round Lips")
        page.wait_for_timeout(1000)
        page.select_option('select[name="voice_tones"]', value="Confident")
        page.wait_for_timeout(1000)
        page.select_option('select[name="common_types_eyebrow_shapes"]', value="Soft Arched Eyebrows")
        page.wait_for_timeout(1000)
        page.select_option('select[name="common_jawline_shapes"]', value="Round Jawline")
        page.wait_for_timeout(1000)
        page.select_option('select[name="common_types_smiles"]', value="Broad Smile")


        page.wait_for_timeout(1000)
        print("hai")
        page.select_option('select[name="countryCode1"]', value="+358")
        page.locator('input[name="phoneNo"]').fill("1234556789893")
        print("hai")
        page.wait_for_timeout(1000)
        page.select_option('select[name="countryCode2"]', value="+358")
        page.locator('input[name="agentPhone"]').fill("1234556789893")
        page.wait_for_timeout(1000)
        page.select_option('select[name="countryCode3"]', value="+358")
        page.locator('input[name="pr_phoneNo"]').fill("1234556789893")

        page.wait_for_timeout(3000)
        page.locator("//input[@placeholder='Enter your skills in details. in maximum 200 characters.']").fill("Acting")
        
        page.locator("//input[@placeholder='Enter your trainings in details. in maximum 200 characters.']").fill("Acting")
        page.locator("//input[@placeholder='Enter your awards in details. in maximum 200 characters.']").fill("Acting")

        page.wait_for_timeout(1000)

        page.select_option('select[name="country"]', value="Afghanistan")
        page.select_option('select[name="state"]', value="Badakhshan")
        page.select_option('select[name="city"]', value="Ashkāsham")
        print("Hello")
        page.locator('[name="number_of_movies"]').fill("12")
        page.wait_for_timeout(1000)
        page.locator('[name="number_of_television_roles"]').fill("12")
        page.wait_for_timeout(1000)
        page.locator('[name="number_of_theater_roles"]').fill("12")
        page.wait_for_timeout(2000)
        page.get_by_role("button",name="Save")
        page.wait_for_timeout(10000)

        print("The profile updated successfully")
        

        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_simple_login()
