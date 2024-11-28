from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the target URL
driver.get('https://jqueryui.com/droppable/')

# Switch to the frame containing the drag and drop elements
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, '.demo-frame'))

# Locate the source and target elements
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')

# Perform the drag and drop operation
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

# Optional: Pause to visually confirm the operation
time.sleep(3)

# Close the WebDriver
driver.quit()

