from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('/usr/bin/chromedriver')
action = ActionChains(driver)
time.sleep(1)

driver.get('https://www.amazon.com')
time.sleep(3)

firstmenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
action.move_to_element(firstmenu).perform()
time.sleep(3)

secondmenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a')
secondmenu.click()
time.sleep(3)

name = input("user_name:")
email = input("email:")
password = input("password:")
retype_password = input("check_password:")

ele = driver.find_element_by_name("customerName")
ele.send_keys(name)
time.sleep(3)

ele = driver.find_element_by_id("email")
ele.send_keys(email)
time.sleep(3)

ele = driver.find_element_by_id("password")
ele.send_keys(password)
time.sleep(3)

ele = driver.find_element_by_id("passwordCheck")
ele.send_keys(retype_password)
time.sleep(3)

ele = driver.find_element_by_id("continue")
ele.click()
time.sleep(3)

#driver.quit()