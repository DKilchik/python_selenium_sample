from .base_test import BaseTest
from pages import CataloguePage

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