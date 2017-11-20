"""
Selenium script to open the browser, print the title and close the browser

Note: Make sure that geckodriver is available in the scripts path.
Geckodriver is designed to drive gecko-based web browser, like Mozilla Firefox.

Download the appropriate geckodriver based on your platform from below download page
Download Page: https://github.com/mozilla/geckodriver/releases
"""

import time
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://www.inmar.com/")
print(browser.title)

if("Inmar" in browser.title):
    print("\nHurry!!!! Launched Inmar home page using selenium.\n")
    time.sleep(5)
    print("Closing the browser!!")
    browser.quit()
    
