from data_Reader.read_Properties import ReadConfig
from selenium.webdriver.common.by import By
from features.lib.pages.base_page_object import BasePage
from data_Reader.read_Environment import ReadEnvironment
base_URL = ReadConfig.get_application_url()
user_Name = ReadEnvironment.get_concert_user_name()
password = ReadEnvironment.get_concert_password()


class LoginPage(BasePage):
    locator_dictionary = {
        "username": (By.ID, 'username'),
        "password": (By.ID, 'password'),
        "login_button": (By.ID, 'kc-login'),
        "title": (By.XPATH, '//title'),
        "logout": (By.ID, 'Logout'),
        "user_button": (By.ID, 'UserButton')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url=base_URL)

    def login(self):
        self.find_element(*self.locator_dictionary['username']).click()
        self.find_element(*self.locator_dictionary['username']).send_keys(user_Name)
        self.find_element(*self.locator_dictionary['password']).click()
        self.find_element(*self.locator_dictionary['password']).send_keys(password)
        self.find_element(*self.locator_dictionary['login_button']).click()

    def get_title(self):
        return self.browser.title

    def click_user_button(self):
        self.find_element(*self.locator_dictionary['user_button']).click()

    def click_logout(self):
        self.find_element(*self.locator_dictionary["logout"]).click()
