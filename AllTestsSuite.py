import os
import unittest
from HtmlTestRunner import HTMLTestRunner
from HomePageTest import HomePageTest

# get the directory path to output report file
dir = os.getcwd()

# Load tests into variables
homepage_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Combine all loaded tests into a suite to be run
all_test_suite = unittest.TestSuite([homepage_test])

# open the report file
outfile = open(dir + "SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(output="AllTestsReport")

# run the suite using HTMLTestRunner
runner.run(all_test_suite)