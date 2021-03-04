from time import sleep

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\Study\Chrome Driver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com")

# Sign In using Facebook login

sleep(5)
log_in_button = driver.find_element_by_xpath(
    '//*[@id="t--1032254752"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
log_in_button.click()
sleep(5)

more_login_options = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div[1]/div/div[3]/span/button')
more_login_options.click()
sleep(5)

facebook_login = driver.find_element_by_xpath(
    '//*[@id="t-1222506740"]/div/div/div[1]/div/div[3]/span/div[2]')
facebook_login.click()

#  Handles the different windows that pop up

base_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]
driver.switch_to.window(facebook_login_window)

# Adds the FB Credentials to the Pop Up login window

fb_email = driver.find_element_by_xpath('//*[@id="email"]')
fb_password = driver.find_element_by_xpath('//*[@id="pass"]')
fb_email.send_keys("email")
fb_password.send_keys("password")
fb_password.send_keys(Keys.ENTER)
sleep(5)
fb_confirm = driver.find_element_by_name("__CONFIRM__")
fb_confirm.click()

# Switches to the main window and handles the pop ups

driver.switch_to.window(base_window)
allow_location_button = driver.find_element_by_xpath('//*[@id="t-1222502240"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="t-1245602240"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# 100 Loops as per free Tinder limits
for n in range(100):

    # Liking profiles with 1 second delay
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    # Catches exception for already liked profiles
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Adds extra 2 second delay for slow loading pages/profiles
        except NoSuchElementException:
            sleep(2)

driver.quit()
