from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


MAIN_MENU = (By.XPATH, "//div[@class='assistant-mobile']")
OFF_PLAN = (By.XPATH, "//a[@wized='mobileTabProperties' and @class='menu-link w-inline-block w--current']")
SETTINGS = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")
CHANGE_PWD = (By.XPATH, "//div[@class='setting-text' and text()='Change password']")
NEW_PASSWORD = (By.CSS_SELECTOR, "input#Enter-new-password")
REPEAT_PWD = (By.CSS_SELECTOR, "input#Repeat-password")
CHANGE_PWD_BTN = (By.CSS_SELECTOR, "//div//a[text()='Change password' and @class='submit-button-2 w-button']")


@given('Open the main page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Log in to the page')
def login(context):
    context.driver.get('https://soft.reelly.io/sign-up')
    context.driver.find_element(By.XPATH, "//div[@wized='signinButtonSignup' and text()='Sign in']")
    sleep(5)
    context.driver.find_element(By.XPATH, "//input[@class='input w-input' and @wized='emailInput']").send_keys("jyoti.m.dewangan@gmail.com")
    context.driver.find_element(By.XPATH, "//input[@class='input w-input' and @placeholder='Password']").send_keys("jd91183")
    context.driver.find_element(By.XPATH, "//a[@wized='loginButton' and text()='Continue']").click()


@when('Click on settings option')
def click_settings(context):
    context.driver.find_element(*SETTINGS).click()


@when('Click on Change password option')
def click_change_password(context):
    context.driver.find_element(*CHANGE_PWD).click()




#actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
  #  assert 'Sign into your Target account' in actual_text, f'Error! Text Sign into your Target account not in {actual_text}'



