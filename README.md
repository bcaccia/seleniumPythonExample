# seleniumPythonExample

This is a sample Selenium Test suite written in Python for the website https://bcacciaaudio.com/

## What does it demonstrate
* How to access and test different types of web elements.
* Setting up a class that will allow selection of desired browser for cross-browser testing or execution on Selenium Grid.
* Using the Python `pytest` library to create a test suite that avoids code duplication by using fixtures.

## Requirements
* `pip install selenium`
* `pip install pytest`
* `pip install pytest-html`

## Set Browser target

Edit the following fixture in the `conftest.py` file to only contain the browser(s) you want to test.
The current options are:
* `chrome`
* `firefox`
* `remoteChrome` (for Selenium Grid)
* `remoteFirefox` (for Selenium Grid)

```
@pytest.fixture(params=["chrome", "firefox"],scope="class")
```

## Running tests

Enter the test directory and run:
`pytest`

To run the tests and generate an HTML report:
`pytest --html=NameOfResultsFile.html`