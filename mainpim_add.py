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
        self.driver.get(self.url)

        self.driver.find_element(by=By.NAME, value=Nithya_Locators(
        ).username_input_box).send_keys(Nithya_Data().username)
        self.driver.find_element(by=By.NAME, value=Nithya_Locators(
        ).password_input_box).send_keys(Nithya_Data().password)
        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().submit_button).click()

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().pim_locator).click()

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().add_button).click()

        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Nithya_Locators(
        ).emp_first_name).send_keys(Nithya_Data().firstName)

        self.driver.find_element(by=By.NAME, value=Nithya_Locators(
        ).emp_last_name).send_keys(Nithya_Data().lastName)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().emp_id).send_keys(Nithya_Data().emp_id)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().save_button).click()
        sleep(5)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().nick_name).send_keys(Nithya_Data().nick_name)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().other_id).send_keys(Nithya_Data().other_id)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().ssn_number).send_keys(Nithya_Data().ssn_number)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().sin_number).send_keys(Nithya_Data().sin_number)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().driver_licence_number).send_keys(Nithya_Data().license_number)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().license_expiry_data).send_keys(Nithya_Data().expiry_date)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().date_of_birth).send_keys(Nithya_Data().date_of_birth)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().gender_female).click()

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().military_service).send_keys(Nithya_Data().military_service)

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().save_one).click()

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().blood_type).click()  # pending

        self.driver.find_element(
            by=By.XPATH, value=Nithya_Locators().save_two).click()
        sleep(4)

        self.driver.quit()
        print("employee personal details addeed successfully")


n = Nithya(Nithya_Data().url)
n.login()
