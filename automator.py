from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()

with open('links.txt', 'r') as f:
    links = f.readlines()
    
driver = webdriver.Edge()
for link in links:
    driver.get(link)
    download_button = driver.find_element(By.CSS_SELECTOR, "#download-url")
    download_button.click()
