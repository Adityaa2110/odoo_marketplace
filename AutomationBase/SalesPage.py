import time
from telnetlib import EC

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SalesPage():

    def __init__(self, driver):
        self.driver = driver

    Menu = (By.XPATH, "/html/body/header/nav/div[1]/button")
    Seller_dashboard = (By.LINK_TEXT, "Seller Dashboard")
    Sales = (By.XPATH,"//div[2]/div[2]/button")
    Orders = (By.XPATH,"//div[2]/div[2]/div/a[text()='Orders']")
    Search_order = (By.XPATH,"//div[1]/div[1]/div/input")
    Select_searched_order = (By.XPATH, "//ul/li[1]/a[2]/b[1]")
    Ordered_product = (By.XPATH,"//ul/li[3]/div/div[2]/div/span[text()='Sales Order']")
    APPROVE_BUTTON = (By.XPATH, "//div[1]/div[1]/div[1]/button/span[text()='Approve']")
    SHIP_NOW_BUTTON = (By.XPATH, "//div[1]/div[1]/div[1]/button/span[text()='Ship Now']")
    VALIDATE_BUTTON = (By.XPATH, "//div[1]/div[1]/div[1]/button/span[text()='Validate']")
    MARKDONE_BUTTON = (By.XPATH, "//span[text()='Mark Done']")
    DONE_BUTTON = (By.XPATH,"//div/footer/button[1]")

    def menu(self):
        self.driver.find_element(*SalesPage.Menu).click()
        time.sleep(2)

    def sellerdashboard(self):
        self.driver.find_element(*SalesPage.Seller_dashboard).click()
        time.sleep(2)

    def sale(self):
        self.driver.find_element(*SalesPage.Sales).click()
        time.sleep(2)

    def orders(self):
        self.driver.find_element(*SalesPage.Orders).click()
        time.sleep(2)

    def search_order(self,order_number):
        search_input = self.driver.find_element(*SalesPage.Search_order)
        search_input.send_keys(order_number)
        search_input.send_keys(Keys.RETURN)
        time.sleep(2)

    def select_searched_order(self):
        print("Waiting for the searched order element to be clickable")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SalesPage.Select_searched_order)
            ).click()
            print("Clicked on the searched order element")
        except NoSuchElementException:
            print("Searched order element not found.")
        except Exception as e:
            print(f"An error occurred: {e}")



    def order_Product(self):
        self.driver.find_element(*SalesPage.Ordered_product).click()
        time.sleep(2)
        print(f"Searching for element with locator: {SalesPage.Select_searched_order}")



    def click_approve_button(self):
        try:
            approve_button = self.driver.find_element(*SalesPage.APPROVE_BUTTON)
            approve_button.click()
        except NoSuchElementException:
            print("Approve Button not found, skipping to next step")
        time.sleep(2)


    def click_ship_now_button(self):
        try:
            ship_now_button = self.driver.find_element(*SalesPage.SHIP_NOW_BUTTON)
            ship_now_button.click()
        except NoSuchElementException:
            print("Ship Now button not found, skipping to next step")
        time.sleep(2)


    def click_validate_button(self):
        try:
            validate_button = self.driver.find_element(*SalesPage.VALIDATE_BUTTON)
            validate_button.click()
        except NoSuchElementException:
            print("Validate button is not clickable,as quantity of product is not available ")
        time.sleep(2)


    def click_markdone_button(self):
        try:
            confirm_button = self.driver.find_element(*SalesPage.MARKDONE_BUTTON)
            confirm_button.click()
            print("Sales order is Marked Done")
        except NoSuchElementException:
            print("Salesorder is already Marked Done")
        time.sleep(2)


    def click_done_button(self):
        try:
            done_button = self.driver.find_element(*SalesPage.DONE_BUTTON)
            done_button.click()
            print("Sales order is succcessfully DONE")
        except NoSuchElementException:
            print("Sales order is already DONE")

        self.driver.quit()







