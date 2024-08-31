

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Visit the specified URL
driver.get('https://www.saucedemo.com')

# Enter the username
username_field = driver.find_element(By.ID,'user-name')
username_field.send_keys('standard_user')

# Enter the password
password_field = driver.find_element(By.ID,'password')
password_field.send_keys('secret_sauce')

# Click the login button
login_button = driver.find_element(By.ID,'login-button')
login_button.click()

# Fetch the title of the webpage
title_of_webpage = driver.title
print(f"Title of the webpage: {title_of_webpage}")

# Fetch the current URL of the webpage
current_url_of_webpage = driver.current_url
print(f"Current URL of the webpage: {current_url_of_webpage}")

# Extract the entire contents of the webpage and save it in a text file
with open("webpage_task_11.txt", "w") as file:
    file.write(driver.page_source)



def file(name,content):
    fil = open(name,"w")
    fil.write(content)



# fetch the current url of the webpage of the webpage and save it in a text file
file("current_url.txt",current_url_of_webpage)


# fetch the title of the webpage and save it in a text file
file("title.txt",title_of_webpage)

# Close the browser session
driver.quit()
