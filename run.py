from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from tests.rooms import first_room, second_room, third_room, fourth_room, fifth_room, sixth_room

def get_driver(headless=False):
    options = Options()
    options.add_experimental_option("detach", True)
    if headless:
        options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def start_bot():
    driver = get_driver()
    driver.get("https://csati.nemestamas.hu/")

    first_room(driver)
    second_room(driver)
    third_room(driver)
    fourth_room(driver)
    fifth_room(driver)
    sixth_room(driver)
    # driver.quit()

start_bot()