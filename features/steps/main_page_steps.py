from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")


@given('Open Target main page')
def open_target(context):
    context.app.main_page.open_main()


@when("Search for {item}")
def search_product(context, item):
    context.app.header.search_product(item)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
    # Add multiple:
    # add_cart_btns = context.driver.find_elements(*ADD_TO_CART_BTN)
    # for btn in add_cart_btns[:5]:
    #     btn.click() # => will click on the first 5 buttons 1 by 1
    # add_cart_btns[4].click() # => will only click on the 5th Add to cart btn


@when('Store product name')
def store_product_name(context):
    context.wait.until(
        EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not present on the page'
    )