"""
Selenium Test to login to Qxf2 Tutorial Page and assert the title
"""

import os
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# The driver.get method will navigate to a page given by the URL
driver.get("http://localhost/selenium-tutorial-main.html")
# Create a screenshots directory if not present
if not (os.path.exists('./tests/screenshots')):
    os.makedirs('./tests/screenshots')
# Save screenshot in the created directory
driver.save_screenshot('./tests/screenshots/Qxf2_Tutorial_page.png')
# Assert the Page Title
assert "Qxf2 Services: Selenium training main" in driver.title
# Close the browser window
driver.close()
