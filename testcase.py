import unittest
import HtmlTestRunner
import time
from selenium import webdriver

class ViewProductDetails(unittest.TestCase):
    # declare variable to store the URL to be visited
    base_url='http://localhost:8081/'


    # --- Pre - Condition ---
    def setUp(self):

        # declare and initialize driver variable
        self.driver=webdriver.Chrome(executable_path='workspace/automationdocker/chromedriver')        
        # browser should be loaded in maximized window
        self.driver.maximize_window()
        # driver should wait implicitly for a given duration, for the element under consideration to load.
        # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
        self.driver.implicitly_wait(300000000000)  #10 is in seconds

    # --- Steps for AMZN_Search_TC_001 ---
    def test_load_home_page(self):        
        # to initialize a variable to hold reference of webdriver instance being passed to the function as a reference.
        driver=self.driver
        # to load a given URL in browser window
        driver.get(self.base_url)  
        print(driver.title)      
        # test whether correct URL/ Web Site has been loaded or not
        self.assertIn("Space Science Website Template",driver.title)

    # --- Steps for AMZN_Search_TC_002 ---
    def test_signup(self):        

        self.driver.get('http://localhost:8081/contact.html')         
        searchTextBox=self.driver.find_element_by_xpath('//*[@id="body"]/div/div/form/input[1]')
        searchTextBox.clear()
        searchTextBox.send_keys('yosra')
        
        searchTextBox=self.driver.find_element_by_xpath('//*[@id="body"]/div/div/form/input[2]')
        searchTextBox.clear()
        searchTextBox.send_keys('yosra@gmail.com')
        searchTextBox=self.driver.find_element_by_xpath('//*[@id="submit"]')
        searchTextBox.click
           
    def tearDown(self):
        # to close the browser
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
