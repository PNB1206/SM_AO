import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['GC','FF'], scope='class')
def init_driver(request):
    if request.param == "GC":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "FF":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    web_driver.get("https://smartmoney.angelone.in/login/")
    web_driver.set_page_load_timeout(30)
    web_driver.maximize_window()

    request.cls.driver = web_driver

    yield
    web_driver.quit()

