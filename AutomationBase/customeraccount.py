import time
from selenium.webdriver.support import expected_conditions as EC

import self
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class customeraccount():

    def __init__(self, driver):
        self.driver = driver

    Email = (By.ID, "login")
    Password = (By.ID, "password")
    Login_button = (By.XPATH, "//*[@id='wrapwrap']/main/div[1]/form/div[3]/button")

    def email(self, enter_email):
        try:
            # Wait for the email input field to be visible
            emailID = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(customeraccount.Email)
            )
            emailID.send_keys(enter_email)
            print(f"Entered email: {enter_email}")
            time.sleep(1)
        except Exception as e:
            print(f"Failed to find email element: {e}")

    def password(self, enter_password):
        try:
            password = self.driver.find_element(*customeraccount.Password)
            password.send_keys(enter_password)
            time.sleep(2)
        except Exception as e:
            print(f"Failed to find password element: {e}")

    def loginbutton(self):

        try:
            self.driver.find_element(*customeraccount.Login_button).click()
            time.sleep(3)
            if "login" in self.driver.current_url:  # Assuming the URL remains on login page if login fails
                    print("Login failed. Capturing screenshot...")
                    timestamp = time.strftime("%Y%m%d_%H%M%S")
                    screenshot_name = f"screenshot_login_failed_{timestamp}.png"
                    self.driver.save_screenshot(screenshot_name)
                    print(f"Screenshot saved as {screenshot_name}")

            elif "login" in self.driver.current_url:  # Assuming the URL remains on login page if login fails
                print("Login failed. Capturing screenshot...")
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                screenshot_name = f"screenshot_login_failed_{timestamp}.png"
                self.driver.save_screenshot(screenshot_name)
                print(f"Screenshot saved as {screenshot_name}")
            else:
                    print("Login successful.")

        except NoSuchElementException:
                print("No error message element found.")


