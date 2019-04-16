from selenium import webdriver


class WebDriverSelect:

    # return webdriver.Firefox(executable_path = "/home/bcaccia/Downloads/geckodriver")
    # return webdriver.Chrome(executable_path = "/home/bcaccia/Downloads/chromedriver")
    # return webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
    # return webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME)

    @staticmethod
    def choose_driver():
        # Change desired browser target here
        return webdriver.Chrome(executable_path="/home/bcaccia/Downloads/chromedriver")