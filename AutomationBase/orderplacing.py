import time

import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class orderplacing():

    def __init__(self, driver):
        self.driver = driver




    Shop = (By.XPATH, "//ul/li[2]/a/span")
    Searching_product = (By.XPATH, "//*[@id='products_grid']/div[1]/form/div/input")
    Select_searching_product = (By.CSS_SELECTOR, "span[class='text-primary']")
    Selected_product = (By.LINK_TEXT, "Cadet Blue Girls T-Shirt")
    Add_to_cart = (By.ID, "add_to_cart")
    Cart_icon = (By.XPATH, '//*[@id="o_main_nav"]/ul[2]/li[2]/a')
    Pay_with_demo = (By.XPATH, '//*[@id="o_demo_express_checkout_container_6"]/button')
    Pay_button = (By.XPATH, '//*[@id="o_payment_demo_modal_6"]/div/div/div[2]/div[2]/button')

    def shop(self):
      self.driver.find_element(*orderplacing.Shop).click()
      time.sleep(2)

    def searching_product(self, enter_product):
       product = self.driver.find_element(*orderplacing.Searching_product)
       product.send_keys(enter_product)  #tshirt
       time.sleep(2)

    def selecting_searching_product(self):
        self.driver.find_element(*orderplacing.Select_searching_product).click()
        time.sleep(2)

    def selected_product(self):
        self.driver.find_element(*orderplacing.Selected_product).click()
        time.sleep(2)

    def add_to_cart(self):
        self.driver.find_element(*orderplacing.Add_to_cart).click()
        time.sleep(2)

    def cart_icon(self):
        self.driver.find_element(*orderplacing.Cart_icon).click()
        time.sleep(2)

    def pay_with_demo(self):
        self.driver.find_element(*orderplacing.Pay_with_demo).click()
        time.sleep(2)

    def pay_button(self):
        try:
            self.driver.find_element(*orderplacing.Pay_button).click()
            time.sleep(2)
            order_number_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="wrap"]/div[1]/div/div[2]/div[2]/h5/em/span[2]'))
            )
            order_number = order_number_element.text
            print(f"Order Number: {order_number}")
        except Exception as e:
            print("Failed to retrieve order number:", e)










