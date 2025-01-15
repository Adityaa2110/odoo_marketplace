import time
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope = 'class')
def setup(request):
    driver = webdriver.Chrome()
    driver.get("http://192.168.5.139:8017/web/login?db=odoo_marketplace")
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    request.cls.driver = driver
    driver.find_element(By.ID, "login").send_keys("admin")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("webkul")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='wrapwrap']/main/div[1]/form/div[3]/button"))).click()
    time.sleep(2)
    yield
    driver.quit()

# @pytest.fixture(scope = 'class')
# def setup2(request):
#      driver = webdriver.Chrome()
#      driver.get("http://192.168.5.139:8017/web/login?db=odoo_marketplace")
#      driver.maximize_window()
#      print(driver.title)
#      print(driver.current_url)
#      request.cls.driver = driver
#      yield
#      driver.quit()

@pytest.fixture(scope = 'class')
def setup3(request):
     driver = webdriver.Chrome()
     driver.get("http://192.168.5.139:8017/web/login?db=odoo_marketplace")
     driver.maximize_window()
     print(driver.title)
     print(driver.current_url)
     request.cls.driver = driver
     yield driver
     driver.quit()