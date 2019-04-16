# seleniumPythonExample

This is a sample Selenium Test suite written in Python for the website https://bcacciaaudio.com/

## What does it demonstrate
* How to access and test different types of web elements.
* Setting up a class that will allow selection of desired browser for cross-browser testing or execution on Selenium Grid.
* Using the Python `unittest` library for assertions. 
* Using `HtmlTestRunner` to generate HTML reports

## Requirements
* `pip install selenium`
* `pip install html-testRunner`

## Set Browser target

```
    @staticmethod
    def choose_driver():
        # Change desired browser target here
        return webdriver.Chrome(executable_path="/home/bcaccia/Downloads/chromedr
```

## Running tests
`python AllTestsSuite.py`