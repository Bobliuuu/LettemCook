from selenium import webdriver
import os

driver = webdriver.Chrome('./chromedriver-mac-arm64/chromedriver')

# Open some tabs for demonstration
driver.get("https://www.example.com")
driver.execute_script("window.open('https://www.google.com');")

# Iterate over all window handles and print tab titles
for window_handle in driver.window_handles:
    driver.switch_to.window(window_handle)
    print(driver.title)

driver.quit()