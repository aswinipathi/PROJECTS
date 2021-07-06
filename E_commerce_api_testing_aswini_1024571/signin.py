from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import selenium


username = input("username:")
password = input("password:")


driver = webdriver.Chrome('/usr/bin/chromedriver')
time.sleep(1)

driver.get('https://www.amazon.in')
time.sleep(2)

firstmenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
firstmenu.click()
time.sleep(3)

sigin_ele = driver.find_element_by_name('email')
sigin_ele.send_keys(logindetails.username)
time.sleep(2)

cont = driver.find_element_by_xpath('continue')
cont.click()
time.sleep(2)

password_ele = driver.find_element_by_name('password')
password_ele.send_keys(logindetails.password)
time.sleep(2)

login_ele = driver.find_element_by_id('signInSubmit')
login_ele.click()
time.sleep(2)

driver.quit()