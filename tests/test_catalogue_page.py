import pytest
import allure
from .base_test import BaseTest
from pages import CataloguePage
from utilities.allure import Given,When,Then,And,then
"""
    These tests are created only for demonstration of Page Object pattern usage.
    Test-design techniques are not implemented in this set. 
    The test structure is also far from ideal and can include basic anti-patterns.
    This version doesn't use builder pattern and fluent interface pattern,
    witch are very popular and are integrated in most of frameworks.
"""


class TestAddingItemsToBasket(BaseTest):
    
    
    ### Approach 1:                                                              ### 
    ### This is an simplified version of the test design.                        ###
    ### The assertions are nested into page object classes.                      ###
    ### For allure step implementation is used custom report utility             ###
    ### screen from allure report:https://prnt.sc/fkd559XwqoPj                   ###
    ###                                                                          ###
    ### pros of concept:                                                         ###
    ### simply to read code                                                      ###
    ### no additional blocks,decorators,context managers inside test body        ###
    ### nested assertion statements can be reused                                ###
    ###                                                                          ###
    ### cons of concept:                                                         ###
    ### test structure isn't formalized                                          ###
    ### no guarantee of atomic test structure(especially in the case of beginners) # 
    ### assertion block doesn't highlighted inside test body                     ###
    ### nested assertions inconveniently to write/edit/debug                     ###
    ### nested assertions break charm of Page Object pattern...                  ###
    ### ... their location is not obvious                                        ###
    def test_guest_can_see_added_item_in_basket_dropdown(self):
        page = CataloguePage(self.driver)
        page.open()
        page.add_item_to_basket()
        page.header.basket_dropdown.open()

        page.header.basket_dropdown.should_be_1_item_in_basket()

        page.header.basket_dropdown.should_be_more_than_0_total_cost()

    ### Approach 2:                                                              ###
    ### assert statement implemented with allure context manager                 ###
    ### Otherwise we will not be able to see assertion steps in allure report    ###
    ### screen from allure report: https://prnt.sc/A2wBbPJeds-l                  ###
    ###                                                                          ###
    ### pros of concept:                                                         ###
    ### still simply to read                                                     ###
    ### assertion block is highlighted in test and it is easy to edit/debug      ###
    ### page object structure isn't broken by additional methods with assertion  ###
    ###                                                                          ###
    ### cons of concept:                                                         ###
    ### test structure isn't formalized                                          ###
    ### no guarantee of atomic test structure(especially in the case of beginners) #
    ### context manager look's alien                                             ### 
    def test_guest_can_see_notification_after_adding_item_in_basket(self):
        page = CataloguePage(self.driver)
        page.open()
        page.add_item_to_basket()
        
        with allure.step("should appear success allert"):
            assert page.check.element_should_appear(
                page.notification_alerts.SUCCESS_ALERT), "Success alert is missing"

    ### Approach 3:                                                              ###
    ### Using the custom allure wrapper tool                                     ###
    ### The result is the same as in previous approach,                          ###
    ### so it's a matter of preferences of code style                            ###
    ### screenshot from allure:https://prnt.sc/AYQSRfsVRG_D                      ###
    def test_guest_can_see_total_cost_increase_after_adding_item_to_basket(self):
        page = CataloguePage(self.driver)
        page.open()
        page.add_item_to_basket()

        @then()
        def total_cost_should_increase_in_header():
            assert page.header.total_cost > 0, "Total cost is 0"

    ### Approach 4:                                                              ###
    ### Adding 'gerkin-like' annotations to allure as steps                      ###
    ### Can be combined with any approach                                        ###
    ### The main advantage is strong structuring of test steps                   ### 
    ### both in code and in allure report                                        ###
    ### This approach can help to avoid popular mistake with creating            ###
    ### non-atomic test structure                                                ###
    ### The cons of concept is additional code                                   ###
    ### Screenshot from allure report: https://prnt.sc/qVcC0FurQ47C              ###
    def test_guest_can_see_deferred_benefit_offer_allert_after_adding_1_item_to_basket(self):

        Given()
        page = CataloguePage(self.driver)
        page.open()

        When()
        page.add_item_to_basket()

        Then()
        @then()
        def deferred_benefit_offer_allert_should_appear():
            assert page.check.element_should_appear(
                page.notification_alerts.DEFERRED_BENEFIR_OFFER_ALERT)
