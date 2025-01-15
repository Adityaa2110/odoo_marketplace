import select
import time
from selenium.webdriver.support import expected_conditions as EC
import self
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class becomeAseller():

    def __init__(self, driver):
        self.driver = driver

    Already_have_account = (By.LINK_TEXT,"Already have an account?")
    Email = (By.ID, "login")
    Password = (By.ID, "password")
    LoginIn = (By.XPATH, "//button[text()='Log in']")
    Become_A_Seller = (By.XPATH, "//div/div[1]/div[2]/a[text()='Become a Seller']")
    Country = (By.ID, 'country_id')
    Profile_url = (By.XPATH, "//*[@id='profile_url']")
    Check_terms_and_condition = (By.ID, 'mp_terms_conditions')
    Submit_button = (By.XPATH, '//*[@id="wrap"]/div/form/div[2]/button')

    def already_have_account(self):
        self.driver.find_element(*becomeAseller.Already_have_account).click()
        time.sleep(2)


    def email(self, enter_email):
       Id = self.driver.find_element(*becomeAseller.Email)
       Id.send_keys(enter_email)
       time.sleep(2)

    def password(self,enter_password):
       passw = self.driver.find_element(*becomeAseller.Password)
       passw.send_keys(enter_password)
       time.sleep(1)

    def login_button(self):
                try:
                    self.driver.find_element(*becomeAseller.LoginIn).click(
                    )

                    error_message = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger").text
                    if "Wrong login/password" in error_message:
                        print("Invalid login/password. Taking screenshot...")
                        timestamp = time.strftime("%Y%m%d_%H%M%S")
                        screenshot_name = f"invalid_details_{timestamp}.png"
                        self.driver.save_screenshot(screenshot_name)
                        print(f"Screenshot saved as {screenshot_name}")
                        raise Exception("Invalid login attempt. Execution stopped.")
                except NoSuchElementException:
                    print("Login successfully")

                except Exception as e:
                   print(f"An unexpected error occurred: {e}")
                   raise e

    def become_a_seller_button(self):
        try:
            # Wait until the "Become a Seller" button is clickable
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(becomeAseller.Become_A_Seller)
            )
            self.driver.find_element(*becomeAseller.Become_A_Seller).click()
            time.sleep(2)
            print("Become a seller button is clicked")
        except TimeoutException:
            print("The Become a Seller button was not clickable within the timeout period.")
        except NoSuchElementException:
            print("Given user account is already a seller")

    def country(self):
        try:
            Dropdown = Select(self.driver.find_element(*becomeAseller.Country))
            Dropdown.select_by_value('3')
            time.sleep(2)
            print("Country is selected")
        except NoSuchElementException:
            print("Country dropdown not found or the option is not available.")

    def profile_url(self, enter_url):
        try:
           url = self.driver.find_element(*becomeAseller.Profile_url)
           url.send_keys(enter_url)
           print("Entered the profile url")
        except NoSuchElementException:
            print ("option not available")

    def check_term_and_conditions(self):
        try:
           self.driver.find_element(*becomeAseller.Check_terms_and_condition).click()
           time.sleep(2)
           print("Checked the terms and conditions")
        except NoSuchElementException:
            print("")

    def submit_form(self):
        try:
            self.driver.find_element(*becomeAseller.Submit_button).click()

            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger"))
            ).text

            if "Could not create a new account" in error_message:
                print("Could not create a new shop, Profile URL already exists. Taking screenshot...")
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                screenshot_name = f"Could_not_create_{timestamp}.png"
                self.driver.save_screenshot(screenshot_name)
                print(f"Screenshot saved as {screenshot_name}")
            else:
                print("Shop request sent successfully.")
        except NoSuchElementException:
            print("Submit button or error message not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        self.driver.quit()



