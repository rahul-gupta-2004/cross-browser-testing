from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.keys import Keys
import time

# Define the URL of the website to be tested
url = "D:/Shortcut folder/rahul/program/cross browser testing/index.html"

# List of browsers to test
browsers = ['chrome', 'firefox', 'edge']

# Loop through each browser
for browser in browsers:
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService())
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService())
    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService())

    # Open the website
    driver.get(url)

    # Check the title of the page
    assert "Cross-Browser Testing" in driver.title

    # Find the button by its ID and click it
    button = driver.find_element(By.ID, "testButton")
    button.click()

    # Wait for a moment to see the action (for demonstration)
    time.sleep(2)

    # Print the browser name and close the browser
    print(f"Test completed successfully on {browser}")
    driver.quit()
