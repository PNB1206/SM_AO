from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

class Basepage:
    def __init__(self, driver):
        self.driver = driver


    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title):
        WebDriverWait(self.driver, 30).until(ec.title_is(title))
        return self.driver.title

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def is_enable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def do_clear(self,by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).clear()


    def get_text(self, by_locator):
        self.wait = WebDriverWait(self.driver, 25)
        element = self.wait.until(ec.visibility_of_element_located(by_locator))
        return element.text


    # To select multiple options from drop down

    def select_all_values(self, names_list, value):
        if not value[0] == 'all':
            for ele in names_list:
                print(ele.text)
                for k in range(len(value)):
                    if ele.text == value[k]:
                        ele.click()
                        break
        else:
            try:
                for ele in names_list:
                    ele.click()
            except Exception as e:
                print(e)



