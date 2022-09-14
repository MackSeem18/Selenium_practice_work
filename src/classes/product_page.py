from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def press_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_same_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == self.browser.find_element(*ProductPageLocators.NOTIFICATION_PRODUCT_NAME).text, \
            "Product name in notification is not equal to added product name"

    def should_be_same_price(self):
        product_price = self.get_price(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text)
        assert product_price == self.get_price(self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text), \
            "Basket price is not equal to the sum of added products prices"
