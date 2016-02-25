from selenium import webdriver

def before_all(context):

#define a Chrome browser instance
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.implicitly_wait(2)

def after_all(context):
    context.browser.quit()
    
