import time

from selenium.webdriver.common.by import By


class SettingPage():

    def __init__(self, driver):
        self.driver = driver

    HomeMenu = (By.XPATH, "//button[@title='Home Menu']")
    Setting = (By.XPATH, "//div/a[text() = 'Settings']")
    MarketPlace = (By.XPATH,"//div[2]/span[@class='app_name']")
    SellerApproval = (By.XPATH, "//input[@id='auto_approve_seller_0']")
    Productapproval = (By.XPATH, "//input[@id='mp_auto_product_approve_0']")
    Quantityapproval = (By.XPATH, "//input[@id='mp_auto_approve_qty_0']")


    def homemenu(self):
        by, value = SettingPage.HomeMenu  # Unpacking the tuple
        self.driver.find_element(by, value).click()

    def setting(self):
        by, value = SettingPage.Setting
        self.driver.find_element(by, value).click()

    def marketplace(self):
        by, value = SettingPage.MarketPlace
        time.sleep(2)
        self.driver.find_element(by, value).click()

    def sellerapproval(self):
        by, value = SettingPage.SellerApproval
        time.sleep(2)
        self.driver.find_element(by, value).click()

    def productapproval(self):
        by,value = SettingPage.Productapproval
        time.sleep(2)
        self.driver.find_element(by, value).click()

    def quantityapproval(self):
        by,value = SettingPage.Quantityapproval
        time.sleep(2)
        self.driver.find_element(by, value).click()

