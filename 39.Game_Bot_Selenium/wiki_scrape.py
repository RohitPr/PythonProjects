from selenium import webdriver

chrome_driver = "D:\Study\Chrome Driver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(count.text)

driver.quit()