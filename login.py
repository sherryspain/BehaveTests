from behave import *
from selenium import webdriver

@given('a valid user name and password')
def step_impl(context):
    context.username="student2"
    context.password="Testing1"
    pass
@when('a valid user clicking on the login button after typing in user name and password')
def step_impl(context):
    context.browser.get("http://demo.mahara.org/")
    context.browser.find_element_by_id("login_login_username").send_keys(context.username)
    context.browser.find_element_by_id("login_login_password").send_keys(context.password)
    context.browser.find_element_by_id("login_submit").click()
    context.browser.implicitly_wait(5)
    pass

@then('logout link should display')
def step_impl(context):
    logout=context.browser.find_element_by_link_text("Logout")
    assert(logout.is_displayed())
    logout.click()
    context.browser.implicitly_wait(5)
    
     
