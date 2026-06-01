from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

class InternetSpeedBot:
    def __init__(self):

        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)

        continue_button = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
        continue_button.click()

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(40)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print("Up: ",self.up)
        print("Down: ",self.down)

bot = InternetSpeedBot()
bot.get_internet_speed()
