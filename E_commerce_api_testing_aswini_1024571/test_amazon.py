# Purpose of the script is to create a methods for all the possibilities

#########################################################################################

# Importing modules 

import pytest
from selenium import webdriver

##########################################################################################

# Chrome driver path, username, password, and url is assigned to a variable

DATA = {"Driver": webdriver.Chrome("/usr/bin/chromedriver"),
        "URL": "https://www.amazon.com",
        "username": "aswinipathi028@gmail.com",
        "password": "12p11@04678"}

############################################################################################

# Class AmazonTest is created and inside class different methods are created

class AmazonTest:

    def __init__(self):

        self.driver = DATA["Driver"]
        self.URL = DATA["URL"]
        self.user = DATA["username"]
        self.password = DATA["password"]
        self.Is_loggedin = False

#############################################################################################

# Method created to get Amazon page

    def getPage(self):

        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.current_url = self.driver.current_url
        print(self.current_url)

        return self.current_url

#############################################################################################

# Method created for SignIn page

    def signIn(self):

        self.nav_account_list = self.driver.find_element_by_id(
            "nav-link-accountList").click()

        self.user_input = self.driver.find_element_by_id("email")
        self.user_input.send_keys(self.user)
        self.continue_button = self.driver.find_element_by_id("continue")
        self.continue_button.click()

        self.pass_input = self.driver.find_element_by_id("password")
        self.pass_input.send_keys(self.password)
        self.submit_button = self.driver.find_element_by_id("signInSubmit")
        self.submit_button.click()

        self.Is_loggedin = True
        return self.Is_loggedin


#################################################################################################################

# Method created to validate user

    def already_user(self):

        self.nav_account_list = self.driver.find_element_by_id(
            "nav-link-accountList").click()

        self.user_input = self.driver.find_element_by_id("email")
        self.user_input.send_keys(self.user)
        self.continue_button = self.driver.find_element_by_id("continue")
        self.continue_button.click()

        self.pass_input = self.driver.find_element_by_id("password")
        self.pass_input.send_keys(self.password)
        self.submit_button = self.driver.find_element_by_id("signInSubmit")
        self.submit_button.click()
        self.Is_loggedin = True
        return self.Is_loggedin

##################################################################################################################

# Method created for color_username_failure

    def color_username_failure(self):

        self.driver.get('https://www.amazon.com')
        self.nav_account_list = self.driver.find_element_by_id(
            "nav-link-accountList").click()

        self.user_input = self.driver.find_element_by_id("ap_email")
        self.user_input.send_keys(self.user)
        self.continue_button = self.driver.find_element_by_id("continue")
        self.continue_button.click()
        element = self.driver.find_element_by_id('auth-error-message-box')
        res = element.value_of_css_property('background-color')
        return res
    
#################################################################################################################

# Method created for color_password_failure

    def color_password_failure(self):
        # self.get = self.getPage()
        self.driver.get('https://www.amazon.com')
        self.nav_account_list = self.driver.find_element_by_id(
            "nav-link-accountList").click()

        self.user_input = self.driver.find_element_by_id("ap_email")
        self.user_input.send_keys(self.user)
        self.continue_button = self.driver.find_element_by_id("continue")
        self.continue_button.click()

        self.pass_input = self.driver.find_element_by_id("ap_password")
        self.pass_input.send_keys(self.password)
        self.signIn_button = self.driver.find_element_by_id("signInSubmit")
        self.signIn_button.click()

        element = self.driver.find_element_by_id('auth-error-message-box')
        res = element.value_of_css_property('background-color')
        return res

ab = AmazonTest()


####################################################################################################
#script deatils

# Script name               :       test_amazon.py
# Script version            :       1.0
# Prepared By               :       aswini.pathi@infinite.com
# Create Date               :       15-june-2021
# Last Modification Date    :       18-june-2021