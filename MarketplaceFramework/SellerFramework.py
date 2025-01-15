import pytest

from AutomationBase.ProductPage import ProductPage
from AutomationBase.SalesPage import SalesPage
from AutomationBase.selleraccount import selleraccount
from MarketplaceFramework.BaseClass import BaseClass2


class TestSellerFramework(BaseClass2):


    @pytest.mark.login
    def test_seller_account(self):
        LoginAccount = selleraccount(self.driver)
        LoginAccount.email("test@test.com")
        LoginAccount.password("webkul")
        LoginAccount.loginbutton()
        LoginAccount.seller_profile_button()
        LoginAccount.logout_button()


    @pytest.mark.productcreation
    def test_product_creation(self):
        Product_Creation = ProductPage(self.driver)
        Login = selleraccount(self.driver)
        Login.email("test@test.com")
        Login.password("webkul")
        Login.loginbutton()
        Product_Creation.product_menu()
        Product_Creation.product()
        Product_Creation.new()
        Product_Creation.product_name("Testseller1")
        Product_Creation.website_Product_category()
        Product_Creation.product_category_name()
        Product_Creation.product_Type()
        Product_Creation.sale_Price(200)
        Product_Creation.save()
        Product_Creation.request_to_Approve()



    def test_order_Approval(self):
        Order_Approval = SalesPage(self.driver)
        Order_Approval.sale()
        Order_Approval.orders()
        Order_Approval.search_order()
        Order_Approval.select_searched_order()
        Order_Approval.order_Product()
        Order_Approval.click_approve_button()
        Order_Approval.click_ship_now_button()
        Order_Approval.click_validate_button()
        Order_Approval.click_markdone_button()
        Order_Approval.click_done_button()







