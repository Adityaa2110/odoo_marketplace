import pytest
import self
from selenium import webdriver

from AutomationBase.becomeAseller import becomeAseller
from AutomationBase.orderplacing import orderplacing
from AutomationBase.createaccount import createaccount
from AutomationBase.customeraccount import customeraccount

@pytest.fixture(scope = 'class')
def setup2(request):
     driver = webdriver.Chrome()
     driver.get("http://192.168.5.139:8017/web/login?db=odoo_marketplace")
     driver.maximize_window()
     print(driver.title)
     print(driver.current_url)
     request.cls.driver = driver
     yield driver
     driver.quit()




@pytest.mark.usefixtures("setup2")
class TestCustomerFrameWork:

    @pytest.mark.login
    def test_login_account(self):
          LoginAccount = customeraccount(self.driver)
          LoginAccount.email("test@webkul.com")
          LoginAccount.password("webkul")
          LoginAccount.loginbutton()

    @pytest.mark.orderplacing
    def test_order_placing(self):
        self.driver.delete_all_cookies()  # Clear cookies before the test
        Order_Placing = orderplacing(self.driver)
        Order_Placing.shop()
        Order_Placing.searching_product("tshirts")
        Order_Placing.selecting_searching_product()
        Order_Placing.selected_product()
        Order_Placing.add_to_cart()
        Order_Placing.cart_icon()
        Order_Placing.pay_with_demo()
        Order_Placing.pay_button()

    @pytest.mark.creation
    def test_account_creation(self):
           self.driver.delete_all_cookies()# Clear cookies before the test
           CreateAccount = createaccount(self.driver)
           CreateAccount.sign_in()
           CreateAccount.donthaveaccount()
           CreateAccount.email("test@webkul.com")
           CreateAccount.name("test")
           CreateAccount.password("webkul")
           CreateAccount.confirmpassword("webkul")
           CreateAccount.save()

    @pytest.mark.becomeseller
    def test_become_A_seller(self):
        self.driver.delete_all_cookies()  # Clear cookies before the test
        become_A_seller = becomeAseller(self.driver)
        become_A_seller.already_have_account()
        become_A_seller.email("test6@webkul.com")
        become_A_seller.password("webkul")
        become_A_seller.login_button()
        become_A_seller.become_a_seller_button()
        become_A_seller.country()
        become_A_seller.profile_url("QQshops")
        become_A_seller.check_term_and_conditions()
        become_A_seller.submit_form()



















