from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def get_chrome_options():
    options = Options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options

def get_webdriver():
    options = get_chrome_options()
    driver = webdriver.Chrome(options=options)
    return driver

def setup():
    driver = get_webdriver()
    url = 'http://across-test.maticson-lab.ru/Login'
    driver.get(url)
    return driver

wd = setup()