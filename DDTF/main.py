from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from Locators import Test_Locators
from Data import WebData
from ExcelFunctions import VishvaaExcelFunctions


excel_file = WebData().excel_file


sheet_number = WebData().sheet_number


vishvaa = VishvaaExcelFunctions(excel_file, sheet_number)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()


driver.get(WebData().url)


driver.implicitly_wait(10)


rows = vishvaa.row_count()


for row in range(2, rows+1):
   username = vishvaa.read_data(row, 6)
   password = vishvaa.read_data(row, 7)


   driver.find_element(by=By.NAME, value=Test_Locators().username_locator).send_keys(username)
   driver.find_element(by=By.NAME, value=Test_Locators().password_locator).send_keys(password)
   driver.find_element(by=By.XPATH, value=Test_Locators().submit_button).click()


   driver.implicitly_wait(10)


   # Main Validation of the TEST CASE either PASS or FAIL is going to happen
   if WebData().dashboard_url in driver.current_url:
       print("SUCCESS : Login success")
       vishvaa.write_data(row, 8, "TEST PASS")
       action = ActionChains(driver)
       action.click(on_element=Test_Locators().logout_button)
       action.perform()
       driver.find_element(by=By.LINK_TEXT, value='Logout').click()


   elif WebData().url in driver.current_url:
       print("FAIL : Login failed")
       vishvaa.write_data(row, 8, "TEST FAIL")
       driver.back()


driver.quit()
