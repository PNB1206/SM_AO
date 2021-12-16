from selenium.webdriver.common.by import By

from PageObjects.base_page import Basepage


class Login_page(Basepage):
    # Locatores
    USER_NAME = (By.XPATH, "//div[@class='floating mb-2']//input[@id='input__email']")
    PASSWORD = (By.XPATH, "//input[@id='input_password']")
    LOGIN_BTN = (By.XPATH, "//span[normalize-space()='Login Now']")

    HOME_TITLE ="Trading Courses: Learn Stock Trading Courses Online | Smart Money by Angel One"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://smartmoney.angelone.in/login/")

    def enter_username(self):
        self.do_clear(self.USER_NAME)
        self.do_send_keys("tc6303341512@gmail.com")

    def enter_password(self):
        self.do_clear(self.PASSWORD)
        self.do_send_keys("q1w2e3r4")

    def click_on_login_button(self):
        self.do_click(self.LOGIN_BTN)

    def get_homepage_title(self):
        self.get_title(self.HOME_TITLE)