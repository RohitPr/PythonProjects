from selenium import webdriver

chrome_driver = "D:\Study\Chrome Driver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.python.org/")

event_time = driver.find_elements_by_css_selector(".event-widget time")
event_name = driver.find_elements_by_css_selector(".event-widget a")

time_list = []
event_list = []
events = {}

for time in event_time:
    time_list.append(time.text)

for name in event_name:
    event_list.append(name.text)

for a in range(len(time_list)):
    event_list[a] = {"time": f"{time_list[a]}", "event": f"{event_list[a+1]}"}


driver.quit()