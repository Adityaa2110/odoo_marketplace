import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ProductPage():

    def __init__(self, driver):
        self.driver = driver


    Menu = (By.XPATH, "/html/body/header/nav/div[1]/button")
    Seller_dashboard = (By.LINK_TEXT, "Seller Dashboard")
    Product_menu = (By.XPATH, "//span[text()='Products']")
    Product = (By.LINK_TEXT,"Products")
    New = (By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/button")
    Product_name = (By.ID, 'name_0')
    Website_product_category = (By.ID,"public_categ_ids_0")
    Product_category_name = (By.XPATH,"//a[text()='Desks']")
    Product_type = (By.ID,'detailed_type_0')
    InternalCategory = (By.XPATH, "//input[@id='categ_id_0']")
    InternalCategory_name = (By.XPATH, "//a[text()='All']")
    Seller = (By.ID, 'marketplace_seller_id_0')
    Seller_name = (By.XPATH,"//a[text()='Blake Clancy']")
    Sale_price = (By.XPATH,"//div/div[2]/div[1]/div/input")
    Save = (By.XPATH,'//i[@class="fa fa-cloud-upload fa-fw"]')
    Request_to_Approve = (By.LINK_TEXT,"Request To Approve")


    def menu(self):
        self.driver.find_element(*ProductPage.Menu).click()
        time.sleep(2)

    def sellerdashboard(self):
        self.driver.find_element(*ProductPage.Seller_dashboard).click()
        time.sleep(2)

    def product_menu(self):
         self.driver.find_element(*ProductPage.Product_menu).click()
         time.sleep(2)

    def product(self):
        self.driver.find_element(*ProductPage.Product).click()
        time.sleep(2)

    def new(self):
        self.driver.find_element(*ProductPage.New).click()
        time.sleep(2)

    def product_name(self,name_of_product):
        search_name = self.driver.find_element(*ProductPage.Product_name)
        search_name.send_keys(name_of_product)
        search_name.send_keys(Keys.RETURN)
        time.sleep(2)
        print(f"name of product: {name_of_product}")

    def website_Product_category(self):
        self.driver.find_element(*ProductPage.Website_product_category).click()
        time.sleep(2)

    def product_category_name(self):
        self.driver.find_element(*ProductPage.Product_category_name).click()
        time.sleep(2)

    def product_Type(self):
        try:
          ProductType = Select(self.driver.find_element(*ProductPage.Product_type))
          ProductType.select_by_visible_text("Consumable")
          time.sleep(2)
        except NoSuchElementException:
          print("No Product_type selected")
        time.sleep(2)

    def internalCategory(self):
        self.driver.find_element(*ProductPage.InternalCategory).click()
        time.sleep(2)

    def internalCategory_name(self):
        self.driver.find_element(*ProductPage.InternalCategory_name).click()
        time.sleep(2)

    def seller(self):
        self.driver.find_element(*ProductPage.Seller).click()
        time.sleep(2)

    def seller_name(self):
        self.driver.find_element(*ProductPage.Seller_name).click()
        time.sleep(2)

    def sale_Price(self,price):
        SalePrice = self.driver.find_element(*ProductPage.Sale_price)
        SalePrice.clear()
        SalePrice.send_keys(price)
        time.sleep(2)

    def save(self):
        self.driver.find_element(*ProductPage.Save).click()
        time.sleep(2)
        print("Product created")

    def request_to_Approve(self):
        try:

            WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable(ProductPage.Request_to_Approve))
            self.driver.find_element(*ProductPage.Request_to_Approve).click()
            time.sleep(2)
            print("Request Approval sent to the Admin")
        except NoSuchElementException:
            print("Request Approval Button Not Found")

