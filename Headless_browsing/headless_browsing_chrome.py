"""
Python Selenium Headless Browsing - Google Chrome Browser
"""




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class SumanHeadlessBrowsing:


   def __init__(self, web_url):


       self.url = web_url


       # Code for headless browsing in Chrome
       chrome_options = webdriver.ChromeOptions()
       chrome_options.add_argument('--headless')


       # Chrome webdriver
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


   def start(self):
       try:
           self.driver.get(self.url)
           sleep(3)
           print("PROCESS-1 : Google Chrome Browser is working")
           return True
       except Exception as error:
           print("ERROR : Automation Failed to Start !")
           return False


   def shutdown(self):
       print("Process-2 : Automation closed")
       self.driver.close()


   def fetch_url(self):
       if self.start():
           return self.driver.current_url
       else:
           return False


   def fetch_title(self):
       if self.start():
           return self.driver.title
       else:
           return False


# main execution function


if __name__ == "__main__":


   url = "https://www.guvi.in/courses/"
   suman = SumanHeadlessBrowsing(url)
   suman.start()
   print(suman.fetch_url())
   print(suman.fetch_title())
   suman.shutdown()
