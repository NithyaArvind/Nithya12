from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class orangehrm_login:

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    username = 'Admin'
    password = 'admin13'
    username_InputBox = 'username'
    password_InputBox = 'password'
    submitButton = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    def __init__(self, url):
        self.url = url
        self.driver.get(self.url)

    def login(self):
        sleep(5)

        initial_cookies = self.driver.get_cookies()

        self.driver.find_element(
            by=By.NAME, value=self.username_InputBox).send_keys(self.username)
        self.driver.find_element(
            by=By.NAME, value=self.password_InputBox).send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value=self.submitButton).click()

        login_cookies = self.driver.get_cookies()

        if (initial_cookies != login_cookies):
            print("SUCCESS [ Navigation ] : Login Successfull")
        else:
            print("login unsuccessful")

        sleep(5)

        self.driver.quit()


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
o = orangehrm_login(url)
o.login()
