"""
HeadlessBrowsing.py


Python Selenium automation codes
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class Data:
   url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
   dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
   username = "Admin"
   password = "admin123"


class Locators:
   username_input_box = "username"
   password_input_box = "password"
   submit_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'




class SumanHeadlessBrowsing(Data, Locators):


   def __init__(self, web_url):
       self.url = web_url


       # enable headless browsing in Google Chrome
       chrome_options = webdriver.ChromeOptions()
       chrome_options.add_argument('--headless')


       # webdriver with headless browsing
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


   def start(self):
       try:
           self.driver.get(self.url)
           sleep(3)
           return True
       except Exception as error:
           print("ERROR : ", error)
           return False


   def shutdown(self):
       self.driver.close()
       return None


   def validate_username_input_box(self):
       username_input_box = self.driver.find_element(by=By.NAME, value=self.username_input_box)
       if username_input_box.is_displayed():
           return True
       else:
           return False


   def validate_password_input_box(self):
       password_input_box = self.driver.find_element(by=By.NAME, value=self.password_input_box)
       if password_input_box.is_displayed():
           return True
       else:
           return False


   def validate_submit_button(self):
       submit_button = self.driver.find_element(by=By.XPATH, value=self.submit_button)
       if submit_button.is_enabled():
           return True
       else:
           return False


   def validate_login(self):
       try:
           self.driver.find_element(by=By.NAME, value=self.username_input_box).send_keys(self.username)
           sleep(2)
           self.driver.find_element(by=By.NAME, value=self.password_input_box).send_keys(self.password)
           sleep(2)
           self.driver.find_element(by=By.XPATH, value=self.submit_button).click()
           if self.driver.current_url == self.dashboard_url:
               return self.driver.current_url
           else:
               return False
       except Exception as error:
           print("ERROR : ", error)
           return False
