from PageObjects.login_page import Login_page
from TestCases.base_test import Base_Test


class Login_Test(Base_Test):
    def test_login(self):
        self.lp = Login_page()
        self.lp.enter_username()
        self.lp.enter_password()
        self.lp.click_on_login_button()
        title = self.lp.get_title()
        assert title == self.lp.HOME_TITLE, "Title not matched"




