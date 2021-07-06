
#Importing webdriver to perform automated browser testing on Chrome browser
from selenium.webdriver import Chrome
#Importing time module
import time
#Importing Action Chains to drag an element, click an element. 
from selenium.webdriver.common.action_chains import ActionChains

#############################################################################################################

#Providing the URL
BASE_URL = "http://automationpractice.com/index.php"
#Providing mail id
EMAIL_ID = "aswinipathi028@gmail.com"

class MyStore(object):

    def __init__(self):
        #Opening the Chrome and getting the MyStore site
        self.driver = Chrome('/usr/bin/chromedriver')
        self.driver.get(BASE_URL)
        self.driver.implicitly_wait(10)

    def signin(self):
        sigin = self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()

        email = self.driver.find_element_by_id('email')
        email.send_keys(EMAIL_ID)

        password = self.driver.find_element_by_id('passwd')
        password.send_keys('12p11@04678')
        
        submit = self.driver.find_element_by_xpath('//*[@id="SubmitLogin"]/span').click()

    def buyproduct(self):
    
        #Navigate to buyproduct Page
        action = ActionChains(self.driver)
        time.sleep(1)

        obj.signin()

        select_women = self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/a')
        action.move_to_element(select_women).perform()
        time.sleep(1)

        #It clicks on buyproduct in page
        T_Shirts = self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/ul/li[1]/ul/li[1]/a')
        T_Shirts.click()

        faded_shirts = self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div[2]/h5/a').click()
    
        quantity = self.driver.find_element_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i').click()
        size = self.driver.find_element_by_xpath('//*[@id="group_1"]/option[text()="L"]').click()
        colour = self.driver.find_element_by_xpath('//*[@id="color_14"]').click()

        add_to_cart = self.driver.find_element_by_xpath('//*[@id="add_to_cart"]/button/span').click()
        proceed_to_checkout = self.driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span').click()
        next_proceed = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span').click() 
        address_proceed = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/form/p/button/span').click() 
        agree = self.driver.find_element_by_xpath('//*[@id="cgv"]').click() 
        shipping_checkout = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/p/button/span').click() 
        payment_proceed = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[2]/div/p/a").click() 
        payment_check_proceed = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/form/p/button/span").click()

obj = MyStore()
obj.buyproduct()