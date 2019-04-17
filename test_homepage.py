import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Use the fixture to apply the desired browser targets to the test class
@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_Homepage(BasicTest):
    # Unit tests
    # @pytest.mark.skip
    def test_load_homepage(self):

        # Declare homepage button that we will check to make sure we are on the homepage
        homepage_button = ".home-icon.active-true"

        # Go to the page
        self.driver.get("https://bcacciaaudio.com/")

        # Find the homepage nav button on the page and ensure it is active
        self.driver.find_element(By.CSS_SELECTOR, homepage_button)

    def test_music_link(self):

        # Declare the link we are going to click
        music_link = "Music"

        # Go to the page
        self.driver.get("https://bcacciaaudio.com/")

        # Find the link and click it
        self.driver.find_element(By.LINK_TEXT, music_link).click()

        # Check the page title to verify it loaded successfully
        WebDriverWait(self.driver, 10).until(EC.title_contains(music_link))

    def test_buy_link(self):

        # Declare the link we are going to click
        buy_link = "Buy Beats"

        # Go to the page
        self.driver.get("https://bcacciaaudio.com/")

        # Find the link and click it
        self.driver.find_element(By.LINK_TEXT, buy_link).click()

        # Check the page title to verify it loaded successfully
        WebDriverWait(self.driver, 10).until(EC.title_contains(buy_link))

    def test_audio_link(self):
        # Declare the link we are going to click
        audio_link = "Audio Post"

        # Go to the page
        self.driver.get("https://bcacciaaudio.com/")

        # Find the link and click it
        self.driver.find_element(By.LINK_TEXT, audio_link).click()

        # Check the page title to verify it loaded successfully
        WebDriverWait(self.driver, 10).until(EC.title_contains(audio_link))

    # This test is meant to fail
    def test_contact_link(self):

        # Declare the link we are going to click
        contact_link = "Contac"

        # Go to the page
        self.driver.get("https://bcacciaaudio.com/")

        # Find the link and click it
        self.driver.find_element(By.LINK_TEXT, contact_link).click()

        # Check the page title to verify it loaded successfully
        WebDriverWait(self.driver, 10).until(EC.title_contains(contact_link))
