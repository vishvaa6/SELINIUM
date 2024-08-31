from selenium import webdriver

# Initialize WebDriver (assuming Chrome)
driver = webdriver.Chrome()

# Navigate to the specified URL
driver.get("https://www.saucedemo.com/")

# Display cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:", cookies_before_login)

# Perform login (replace with actual credentials)
username_field = driver.find_element_by_id("user-name")
password_field = driver.find_element_by_id("password")
login_button = driver.find_element_by_id("login-button")

username_field.send_keys("your_username")  # Replace with actual username
password_field.send_keys("your_password")  # Replace with actual password
login_button.click()

# Display cookies after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:", cookies_after_login)

# Verify if new cookies were generated during login
new_cookies = set(cookie['name'] for cookie in cookies_after_login) - set(cookie['name'] for cookie in cookies_before_login)
if new_cookies:
    print(f"New cookies generated during login: {new_cookies}")
else:
    print("No new cookies generated during login.")

# Perform logout (assuming a logout button exists)
logout_button = driver.find_element_by_id("logout_sidebar_link")
logout_button.click()

# Close the browser session
driver.quit()
