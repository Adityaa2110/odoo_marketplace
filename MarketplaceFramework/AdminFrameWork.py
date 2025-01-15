import pytest
import self

from AutomationBase.SalesPage import SalesPage
from MarketplaceFramework.BaseClass import BaseClass
from AutomationBase.ProductPage import ProductPage
from AutomationBase.productrequestapproval import productrequestapproval


class TestAdminFrameWork(BaseClass):

    @pytest.mark.product
    def test_product_creation(self):
        productpage = ProductPage(self.driver)
        productpage.menu()
        productpage.sellerdashboard()
        productpage.product_menu()
        productpage.product()
        productpage.new()
        productpage.product_name("TestProduct5")
        productpage.website_Product_category()
        productpage.product_category_name()
        productpage.product_Type()
        productpage.internalCategory()
        productpage.internalCategory_name()
        productpage.seller()
        productpage.seller_name()
        productpage.sale_Price(200)
        productpage.save()

    @pytest.mark.approval
    def test_product_request_approval(self):
        Request_Approval = productrequestapproval(self.driver)
        Request_Approval.menu()
        Request_Approval.sellerdashboard()
        Request_Approval.productmenu()
        Request_Approval.product()
        Request_Approval.productname("Testseller1")
        Request_Approval.openproduct()
        Request_Approval.requestbutton()
        Request_Approval.approve()
        Request_Approval.approvevariant()
        Request_Approval.togglebutton()

    @pytest.mark.orderapproval
    def test_order_approval(self):
        Order_Approval = SalesPage(self.driver)
        Order_Approval.menu()
        Order_Approval.sellerdashboard()
        Order_Approval.sale()
        Order_Approval.orders()
        Order_Approval.search_order("S00051")
        Order_Approval.select_searched_order()
        Order_Approval.order_Product()
        Order_Approval.click_approve_button()
        Order_Approval.click_ship_now_button()
        Order_Approval.click_validate_button()
        Order_Approval.click_markdone_button()
        Order_Approval.click_done_button()


























