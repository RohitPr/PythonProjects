from selenium import webdriver
from selenium.webdriver.common.keys import Keys

linkedIn_url = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=109710172&keywords=python%20developer&location" \
               "=Bengaluru%2C%20Karnataka%2C%20India "

chrome_driver = "D:\Study\Chrome Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

# Signs into Linked In using my Credentials

driver.get(linkedIn_url)
sign_in_btn = driver.find_element_by_class_name("nav__button-secondary")
sign_in_btn.click()

email_input = driver.find_element_by_name("session_key")
email_input.send_keys("email")
password = driver.find_element_by_name("session_password")
password.send_keys("password")
password.send_keys(Keys.ENTER)

# Clicks on the first Job and Saves the Job Details to the profile(Did not Apply as this is my Main account)

job = driver.find_element_by_css_selector(".artdeco-entity-lockup__title a")
job.click()
save = driver.find_element_by_css_selector(".jobs-save-button span")
save.click()

driver.quit()
