import time

from selenium import webdriver

chrome_driver = "D:\Study\Chrome Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Webdriver objects to Capture various Website information

cookie = driver.find_element_by_xpath('//*[@id="cookie"]')
cookie_store = driver.find_elements_by_css_selector('#store b')
cookie_meter = driver.find_element_by_id('money')
cookie_data = {}

# Storing the Cookie Shop Data in Dict

for a in range(len(cookie_store) - 1):
    cookie_power = (cookie_store[a].text.split(" - ")[0])
    price = int(cookie_store[a].text.split(" - ")[1].replace(",", ""))
    cookie_data[a] = {
        "power": cookie_power,
        "price": price,
    }


# Automating the game and checking and adding the highest value shop item every Time Interval
def game():
    game_is_on = True
    timeout = time.time() + 60 * 5  # 5 Minutes from now
    while game_is_on:
        cookie.click()
        if time.time() > timeout:
            cookie_count = int(cookie_meter.text.replace(",", ""))
            for item in reversed(range(len(cookie_data))):
                if cookie_count > cookie_data[item]["price"]:
                    cookie_select = driver.find_element_by_id(f"buy{cookie_data[item]['power']}")
                    cookie_select.click()
                    game()


game()
