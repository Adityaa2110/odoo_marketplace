import time
from selenium.webdriver.support import expected_conditions as EC
import self
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class productrequestapproval():

    def __init__(self, driver):
        self.driver = driver

    Menu = (By.XPATH, "/html/body/header/nav/div[1]/button")
    Seller_dashboard = (By.LINK_TEXT, "Seller Dashboard")
    Product_menu = (By.XPATH, "//span[text()='Products']")
    Product = (By.LINK_TEXT, "Products")
    Product_name = (By.XPATH, "//div/div/div/input")
    Select_name = (By.XPATH, '//div/div[1]/div/ul/li[1]/a')
    Open_product = (By.ID,'product_name')
    Request_button = (By.XPATH, "//span[text()='Request To Approve']")
    Approve = (By.XPATH, "//span[text()='Approve']")
    Approve_variant = (By.NAME, 'approve_selected_variant')
    Toggle_button = (By.XPATH, '//button/div/div')

    def menu(self):
        self.driver.find_element(*productrequestapproval.Menu).click()

    def sellerdashboard(self):
        self.driver.find_element(*productrequestapproval.Seller_dashboard).click()
        time.sleep(2)

    def productmenu(self):
        self.driver.find_element(*productrequestapproval.Product_menu).click()
        time.sleep(2)

    def product(self):
        self.driver.find_element(*productrequestapproval.Product).click()
        time.sleep(2)


    def productname(self,name_of_product):
        product_name = self.driver.find_element(*productrequestapproval.Product_name)
        product_name.send_keys(name_of_product)
        product_name.send_keys(Keys.RETURN)
        time.sleep(2)

    def openproduct(self):
        self.driver.find_element(*productrequestapproval.Open_product).click()
        time.sleep(2)

    def requestbutton(self):

       try:
        # Check if "Request To Approve" button is present and click
           request_button = self.driver.find_element(*productrequestapproval.Request_button)
           request_button.click()
           time.sleep(2)
           print("Request is successfully approved")
       except NoSuchElementException:
           print("'Request To Approve' not found. Product is already approved.")

    def approve(self):

       try:
        # Check if "Approve" button is present and click
          approve_button = self.driver.find_element(*productrequestapproval.Approve)
          approve_button.click()
          time.sleep(2)
       except NoSuchElementException:
          print("'Approve' not found. Skipping to next step.")


    def approvevariant(self):
       try:
        # Check if "Approve Variant is present and click"
          self.driver.find_element(*productrequestapproval.Approve_variant).click()
          time.sleep(2)
       except NoSuchElementException:
          print("'Approvevariant' not found. Skipping to next step.")

    def togglebutton(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(productrequestapproval.Toggle_button)  # Replace with the correct selector
            )
            self.driver.find_element(*productrequestapproval.Toggle_button).click()
            print("Product is successfully published")
        except TimeoutException:
            print("Toggle button not found or not clickable.")














