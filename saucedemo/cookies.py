from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a WebDriver instance
driver = webdriver.Chrome()

# Navigate to the SauceDemo website
driver.get("https://www.saucedemo.com/")

# Get cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:")
print(cookies_before_login)
for cookie in cookies_before_login:
    print(f"{cookie['name']}={cookie['value']}")

# Login to the portal
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

# Get cookies after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:")
print(cookies_after_login)
for cookie in cookies_after_login:
    print(f"{cookie['name']}={cookie['value']}")

# Verify cookie generation
if len(cookies_after_login) > len(cookies_before_login):
    print("Cookies were generated during the login process.")
else:
    print("Cookies were not generated during the login process.")

# Perform logout
logout_button = driver.find_element(By.ID, "react-burger-menu-btn")
logout_button.click()
logout_link = driver.find_element(By.ID, "logout_sidebar_link")
logout_link.click()

# Close the browser
driver.quit()