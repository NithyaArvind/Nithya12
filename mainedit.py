from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Nithya_Data
from Test_Locators.locators import Nithya_Locators
from selenium.webdriver.support.ui import Select
from time import sleep


class Nithya:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()))
        # self.driver.maximize_window()
        # self.driver.get(url)

    def login(self):

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.url)  # doubt

        self.driver.find_element(by=By.NAME, value=Nithya_Locators(
        ).username_input_box).send_keys(Nithya_Data().username)
        self.driver.find_element(by=By.NAME, value=Nithya_Locators(
        ).password_input_box).send_keys(Nithya_Data().password)
        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().submit_button).click()

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().pim_locator).click()

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().edit_paul_locator).click()

        self.driver.find_element(by=By.NAME, value=Nithya_Locators(
        ).middle_name_locator).send_keys(Nithya_Data().middleName)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().edit_save_locator).click()

        print("successfully edited")

        sleep(10)

        self.driver.quit()


n = Nithya(Nithya_Data().url)
n.login()
