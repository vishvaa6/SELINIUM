"""
test_OrangeHRM.py


Test Case file for HeadlessBrowsing.py
"""


from headless_browsing import SumanHeadlessBrowsing
from headless_browsing import Data
import pytest


suman = SumanHeadlessBrowsing(Data.url)


def test_start():
   assert suman.start() == True
   print("SUCCESS : Automation started")


# Test Case-1 : Validate Username Input Box
def test_validate_username_input_box():
   assert suman.validate_username_input_box() == True
   print("SUCCESS : Username Input Box is Visible")




# Test Case-2 : Validate Password Input Box
def test_validate_password_input_box():
   assert suman.validate_password_input_box() == True
   print("SUCCESS : Password Input Box is Visible")




# Test Case-3 : Validate Submit Button
def test_validate_submit_button():
   assert suman.validate_submit_button() == True
   print("SUCCESS : Submit Button is Displayed & Enabled")


# Test Case 4 : Validate Login
def test_validate_login():
   assert suman.validate_login() == Data().dashboard_url
   print("SUCCESS : Login success to Dashboard URL {url}".format(url=Data().dashboard_url))


def test_stop():
   assert suman.shutdown() == None
   print("SUCCESS : Automation Testing Completed")
