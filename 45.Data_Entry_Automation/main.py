from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

chrome_driver_path = "D:\Study\Chrome Driver\chromedriver.exe"

zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A" \
             "-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C" \
             "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A" \
             "%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse" \
             "%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D" \
             "%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min" \
             "%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D "
user_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.190 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
}

response = requests.get(url=zillow_url, headers=user_headers)
rent_data = response.text

# Extracts the data from Zillow and stores required data in different Lists

soup = BeautifulSoup(rent_data, "lxml")

link_elements = soup.select(".list-card-top a")
links = []
for link in link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)

address_elements = soup.select(".list-card-info address")
addresses = [address.get_text().split(" | ")[-1] for address in address_elements]

price_elements = soup.select(".list-card-details li")
prices = [price.get_text().split("+")[0].replace("bds", "") for price in price_elements if "$" in price.text]

driver = webdriver.Chrome(chrome_driver_path)

# Opens the Form and sends required data Automatically

driver.get("https://forms.gle/h9xbtrbMaFMH5Y6V6")
sleep(5)

for a in range(len(links)):
    address_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(addresses[a])
    rent_input.send_keys(prices[a])
    link_input.send_keys(links[a])
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    sleep(2)
    submit_button.click()
    sleep(5)
    submit_next = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_next.click()
    sleep(5)
