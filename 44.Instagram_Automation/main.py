from time import sleep

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

TARGET_ACCOUNT = "igndotcom"
USERNAME = "email"
PASSWORD = "password"
chrome_driver_path = "D:\Study\Chrome Driver\chromedriver.exe"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://instagram.com/")
        sleep(5)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)
        account_dialog = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button')
        account_dialog.click()
        sleep(5)
        notification_dialog = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification_dialog.click()

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")

        sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        # This will scroll the Pop up Followers to load a bigger list of followers
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            # This will check if we have already followed the person and are getting a unfollow request
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()
