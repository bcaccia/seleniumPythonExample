import unittest
from WebDriverSelect import WebDriverSelect
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # Instantiate a driver instance
        cls.driver = WebDriverSelect.choose_driver()
        # Maximize the browser window
        cls.driver.maximize_window()

    def test_homepage(self):

        # Declare all page elements
        homepage_button = ".home-icon.active-true"

        # Go to the page
        self.driver.get("https://bcacciaaudio.com/")

        # Find the homepage nav button on the page and ensure it is active
        self.driver.find_element(By.CSS_SELECTOR, homepage_button)

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()
