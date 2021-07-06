##############################################################################################

# Purpose of the script

##############################################################################################

# 1.Automating the website using automation testing with python,selenium

##############################################################################################

# contents of the script:

##############################################################################################

# 1.Install the selenium

# 2.Write the python code with selenium webdriver using chrome

# 3.Creating a pages folder having __init__.py , result.py, search.py in it.

# 4.In tests folder  test_web.py change the code and create config.json with time and browser

# 5.In tests create the confest.py where write the logic for fixtures, browser 

#################################################################################################

"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import pytest
import logging
import sys, os
from test_amazon import AmazonTest


logging.basicConfig(filename="e_commerce.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logging.warning('script is being executed')
#Creating an object
logger=logging.getLogger()
logger.setLevel(logging.INFO)

amazon_class_instance = AmazonTest()
# logger.info('checking the test_basic_duckduckgo_search testcase')

#####################################################################################################

# Created a class called AmazonTest and methods are created inside class

class TestAmazonTest:

######################################################################################################

# Method to test the Amazon page

    def test_getPage(self): 
        assert amazon_class_instance.getPage() == "https://www.amazon.com/"

#######################################################################################################

# Method to test user 

    def test_user(self):
        amazon_class_instance.already_user()
        assert 

    def test_user(self):
      assert amazon_class_instance.already_user() == True

########################################################################################################

# Method created to test the incorrect user

    def test_incorrect_username(self):
      # colour = amazon_class_instance.color()
      assert amazon_class_instance.color_username_failure() == 'rgba(255, 255, 255, 1)'

#########################################################################################################

# Method created to test the incorrect password

    def test_incorrect_password(self):
      assert amazon_class_instance.color_password_failure() == 'rgba(255, 255, 255, 1)'
      


##########################################################################################################

#script deatils

# Script name               :       testcases_amazon.py
# Script version            :       1.0
# Prepared By               :       aswini.pathi@infinite.com
# Create Date               :       15-june-2021
# Last Modification Date    :       18-june-2021