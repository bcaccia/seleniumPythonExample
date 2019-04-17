import pytest
from selenium import webdriver


# This method allows the user to select which browsers to run their tests against. The desired test targets
# must be placed in the param brackets. All declared targets between the brackets will be tested against.
@pytest.fixture(params=["chrome", "firefox"],scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path = "/home/bcaccia/Downloads/chromedriver")
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path = "/home/bcaccia/Downloads/geckodriver")
    if request.param == "remoteFirefox":
        web_driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
    if request.param == "remoteChrome":
        web_driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME)
    request.cls.driver = web_driver
    request.cls.driver.maximize_window()
    yield
    web_driver.close()
