from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver,search_bt):
    return WebDriverWait(driver,10).until(lambda s: s.find_element(*search_bt))
    