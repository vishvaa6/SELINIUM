from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (assuming ChromeDriver is installed and available in PATH)
driver = webdriver.Chrome()

# Open the specified URL
driver.maximize_window()
driver.get("https://www.cowin.gov.in/")

# Click on "Create FAQ"
create_faq = driver.find_element(By.XPATH,"/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a")
create_faq.click()

# Switch to the new window
window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])

# Fetch the window ID and display it
window_id = driver.current_window_handle
print(f"Window/Frame ID: {window_id}")

# Close the new window
driver.close()


# Switch back to the main window
driver.switch_to.window(window_handles[0])

# Click on "Partners"
partners = driver.find_element(By.XPATH,"/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a")
partners.click()

# Switch to the new window
window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])

# Fetch the window ID and display it
window_id = driver.current_window_handle
print(f"Window/Frame ID: {window_id}")

# Close the new window
driver.close()

# Switch back to the main window
driver.switch_to.window(window_handles[0])

# Verify if returned to the Home page by checking the title
assert "CoWIN" in driver.title

# Close the browser session
driver.quit()
