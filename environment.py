from selenium import webdriver


def before_all(context):
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.maximize_window()
    context.driver = driver


def after_all(context):
    context.driver.quit()
