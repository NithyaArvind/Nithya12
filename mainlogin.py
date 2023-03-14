from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Nithya_Data
from Test_Locators.locators import Nithya_Locators
from time import sleep


class Nithya:

    def __init__(self, url):
        self.driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(url)

    def login(self):

        initial_cookies = self.driver.get_cookies()

        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Nithya_Locators(
        ).username_input_box).send_keys(Nithya_Data().username)
        self.driver.find_element(by=By.NAME, value=Nithya_Locators(
        ).password_input_box).send_keys(Nithya_Data().password)
        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().submit_button).click()

        login_cookies = self.driver.get_cookies()

        if (initial_cookies != login_cookies):
            print("SUCCESS [ Navigation ] : Login Successfull")
        else:
            print("login unsuccessful")

        sleep(10)

        self.driver.quit()


n = Nithya(Nithya_Data().url)
n.login()
