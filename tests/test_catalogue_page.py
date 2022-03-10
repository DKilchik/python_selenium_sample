import pytest
from .base_test import BaseTest
from pages import CataloguePage, LoginPage

"""
    These tests are created only for demonstration of Page Object pattern usage.
    Test-design techniques are not implemented in this set. 
    The test structure is also far from ideal and can include basic anti-patterns.

"""


class TestAddingItemsToBasket(BaseTest):
    
    
    def test_guest_add_item_to_basket(self):
        page = CataloguePage(self.driver)
        page.open()
        page.add_item_to_basket()
        page.header.basket_dropdown.open()

        items_in_basket = page.header.basket_dropdown.items_number
        assert items_in_basket  == 1, "Wrong number of items in basket"

        total_cost = page.header.basket_dropdown.total_cost
        assert total_cost > 0, "Total cost is 0"

    def test_user_add_item_to_basket(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login_form.login()

        catalogue_page = CataloguePage(self.driver)
        catalogue_page.add_item_to_basket()

        total_cost = catalogue_page.header.total_cost
        assert total_cost > 0, "Total cost is 0"

        assert catalogue_page.check.element_will_appear(
            catalogue_page.notification_alerts.SUCCESS_ALERT), "Success alert is missing"