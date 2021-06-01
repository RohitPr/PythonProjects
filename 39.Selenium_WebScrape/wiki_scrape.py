from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = "D:\Study\Chrome Driver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# count.click()

portal_link = driver.find_element_by_link_text("All portals")
# portal_link.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
