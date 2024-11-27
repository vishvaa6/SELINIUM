from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep



class MovingBetweenWindows:


   def __init__(self, web_url):
       self.url = web_url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.dashboard_faq = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[2]/a"
       self.dashboard_partner = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a"


   def windows(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           sleep(3)
           parent_window_handle = self.driver.current_window_handle
           print("Window ID of HomePage : ",parent_window_handle)
           self.driver.find_element(by=By.XPATH, value=self.dashboard_faq).click()
           all_window_handle = self.driver.window_handles
           print(all_window_handle)
           # Iterating over the multiple Windows ID & closing the dashboard window
           for windows in all_window_handle:
               if windows != parent_window_handle:
                   self.driver.switch_to.window(windows)
                   sleep(3)

                   self.driver.close()
                   break
       except Exception as error:
           print("ERROR : ", error)
       finally:
           print("SUCCESS : Automation is success !")
           self.driver.close()






# main execution function
if __name__ == "__main__":


   url = "https://www.cowin.gov.in/"
   vishvaa = MovingBetweenWindows(url)
   vishvaa.windows()
