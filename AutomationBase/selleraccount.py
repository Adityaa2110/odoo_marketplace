import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
import self
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class selleraccount():

    def __init__(self, driver):
        self.driver = driver

    Email = (By.ID, "login")
    Password = (By.ID, "password")
    Login_button = (By.XPATH, "//*[@id='wrapwrap']/main/div[1]/form/div[3]/button")
    Seller_Profile_button = (By.XPATH,"//button[@class='dropdown-toggle py-1 py-lg-0']")
    Logout_Button = (By.XPATH,"//a[text()='Log out']")


    def email(self,enter_email):
            emailID = self.driver.find_element(*selleraccount.Email)
            emailID.send_keys(enter_email)
            time.sleep(1)

    def password(self,enter_password):
            password =self.driver.find_element(*selleraccount.Password)
            password.send_keys(enter_password) # Use an incorrect password for testing
            time.sleep(2)

    def loginbutton(self):
        try:
            self.driver.find_element(*selleraccount.Login_button).click()
            time.sleep(1)

            # Wait for potential error message
            try:
                error_message = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger"))
                ).text

                if "login" in error_message:  # Assuming 'login' indicates a failure message
                    print("Login failed. Capturing screenshot...")
                    timestamp = time.strftime("%Y%m%d_%H%M%S")
                    screenshot_name = f"screenshot_login_failed_{timestamp}.png"
                    self.driver.save_screenshot(screenshot_name)
                    print(f"Screenshot saved as {screenshot_name}")
                    return  # Exit the method after handling the failure

            except TimeoutException:
                # No error message was found, proceed with login success
                print("Login successful.")

        except NoSuchElementException:
            print("Login button not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        # finally:
        #     # Ensure driver quits at the end of the method
        #     self.driver.quit()


    def seller_profile_button(self):
        self.driver.find_element(*selleraccount.Seller_Profile_button).click()
        time.sleep(2)

    def logout_button(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(selleraccount.Logout_Button))
        self.driver.find_element(*selleraccount.Logout_Button).click()

