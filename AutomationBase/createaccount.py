import time

import self
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class createaccount():

    def __init__(self, driver):
        self.driver = driver

    Sign_in = (By.LINK_TEXT,"Sign in")
    Dont_have_account = (By.LINK_TEXT, "Don't have an account?")
    Email = (By.ID, "login")
    Name = (By.ID, "name")
    Password = (By.ID, "password")
    Confirm_Password = (By.ID, "confirm_password")
    Save = (By.XPATH, "//*[@id='wrapwrap']/main/div[1]/form/div[5]/button")



    def sign_in(self):
        self.driver.find_element(*createaccount.Sign_in).click()
        time.sleep(2)

    def donthaveaccount(self):
        self.driver.find_element(*createaccount.Dont_have_account).click()
        # vel = EC.visibility_of_element_located(createaccount.Dont_have_account)
        # WebDriverWait(self,20).until(vel.click())
        time.sleep(2)

    def email(self,write_email):
         email_name=self.driver.find_element(*createaccount.Email)
         email_name.send_keys(write_email)
         time.sleep(2)

    def name(self, write_customer_name):
        name_of_customer = self.driver.find_element(*createaccount.Name)
        name_of_customer.send_keys(write_customer_name)
        time.sleep(2)

    def password(self,write_password):
        password_write = self.driver.find_element(*createaccount.Password)
        password_write.send_keys(write_password)
        time.sleep(2)

    def confirmpassword(self,write_confirm_password):
        confirm_password = self.driver.find_element(*createaccount.Confirm_Password)
        confirm_password.send_keys(write_confirm_password)# Mismatched password
        time.sleep(2)

    def save(self):

        try:
            self.driver.find_element(*createaccount.Save).click()

            # Wait for the error message element to become visible
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger"))
            ).text

            # Check for specific error messages
            if "Passwords do not match" in error_message:
                print("Passwords do not match. Taking screenshot...")
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                screenshot_name = f"password_mismatch_{timestamp}.png"
                self.driver.save_screenshot(screenshot_name)
                print(f"Screenshot saved as {screenshot_name}")

            elif "Another user is already registered" in error_message:
                print("Another user is already registered. Taking screenshot...")
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                screenshot_name = f"already_registered_{timestamp}.png"
                self.driver.save_screenshot(screenshot_name)
                print(f"Screenshot saved as {screenshot_name}")

            else:
                print("Account Creation successful.")

        except TimeoutException:
            print("No specific error message detected, but password might still not match.")

        except NoSuchElementException:
            print("No error message element found.")

    #     finally:
    # # Close the browser regardless of the outcome
    #       self.driver.quit()