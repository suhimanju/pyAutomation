"""
Selenium script in python for checking titles of multiple windows opened;

Note: Make sure that geckodriver is available in the scripts path.
Geckodriver is designed to drive gecko-based web browser, like Mozilla Firefox.

Download the appropriate geckodriver based on your platform from below download page
Download Page: https://github.com/mozilla/geckodriver/releases
"""

import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.seleniumframework.com/Practiceform/")
window_titles = []
print(driver.current_url)
title_before = driver.title
window_titles.append(title_before)
newTab_btn = driver.find_element_by_xpath("//button[@style='background-color:DarkGreen' and @onClick='newBrwTab()']")
newTab_btn.click()
list_window_handles = driver.window_handles #list of windows/tabs opened
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.refresh()
print(driver.current_url)
title_after = driver.title
print(title_after)
window_titles.append(title_after)
print("number of windows open are: " + str(len(list_window_handles)))
for x in range(len(window_titles)):
    print(str(x+1) + ": " +window_titles[x])

time.sleep(10)
print("Quitting!!!!")
driver.quit()
