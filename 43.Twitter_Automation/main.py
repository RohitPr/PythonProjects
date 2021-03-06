import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

TWITTER_EMAIL = "Email"
TWITTER_PASSWORD = "Password"
UP_SPEED = 60
DOWN_SPEED = 60

# Opens Speedtest and checks the download and upload speed

chrome_driver_path = "D:\Study\Chrome Driver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://speedtest.net")
speedtest_start = driver.find_element_by_class_name("start-text")
speedtest_start.click()
time.sleep(60)
speedtest_downspeed = driver.find_element_by_class_name("download-speed")
download_speed = float(speedtest_downspeed.text)
speedtest_upspeed = driver.find_element_by_class_name("upload-speed")
upload_speed = float(speedtest_upspeed.text)
driver.quit()

# If speed lower than specified, opens Twitter and sends a tweet with the download and Upload speed to the ISP

if download_speed < DOWN_SPEED:
    driver.get("https://twitter.com")
    time.sleep(10)
    twitter_login = driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span')
    twitter_login.click()
    time.sleep(5)
    twitter_username = driver.find_element_by_name("session[username_or_email]")
    twitter_username.send_keys(TWITTER_EMAIL)
    twitter_password = driver.find_element_by_name("session[password]")
    twitter_password.send_keys(TWITTER_PASSWORD)
    twitter_password.send_keys(Keys.ENTER)

    tweet = driver.find_element_by_class_name("public-DraftStyleDefault-block")
    tweet.send_keys(
        f"Hey @HathwayBrdband, why my internet speed is {download_speed}Mbps Downoad/{upload_speed} Mbps Upload when you advertise the minimum speed as 100 Mbps Download/ 100 Mbps Upload ")
    tweet_send = driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
    tweet_send.click()
    driver.quit()
