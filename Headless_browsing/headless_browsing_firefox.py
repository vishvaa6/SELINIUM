from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class VishvaaHeadlessBrowsing:

    def __init__(self, web_url):

        self.url = web_url

        # Code for headless browsing in Firefox
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')

        # Firefox webdriver
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    def start(self):
        try:
            self.driver.get(self.url)
            sleep(3)
            print("PROCESS-1 : Firefox Browser is working")
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
    vishvaa = VishvaaHeadlessBrowsing(url)
    vishvaa.start()
    print(vishvaa.fetch_url())
    print(vishvaa.fetch_title())
    vishvaa.shutdown()
