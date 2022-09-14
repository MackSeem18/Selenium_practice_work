from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:

    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")

    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main .price_color")

    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    NOTIFICATION_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:first-child > div >strong")

    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div:last-child > div > p:first-child > strong")




