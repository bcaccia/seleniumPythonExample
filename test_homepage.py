import pytest
from selenium.webdriver.common.by import By

# Use the fixture to apply the desired browser targets to the test class
@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_Homepage(BasicTest):
    # Unit tests
    def test_load_homepage(self):

        # Declare all page elements
        homepage_button = ".home-icon.active-true"

        # Go to the page
        self.driver.get("https://bcacciaaudio.com/")

        # Find the homepage nav button on the page and ensure it is active
        self.driver.find_element(By.CSS_SELECTOR, homepage_button)

    def test_music_link(self):

        # Go to the page
        self.driver.get("https://www.google.com/")

