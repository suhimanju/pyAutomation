"""
Selenium script for filling and submitting the form;

Note: Make sure that geckodriver is available in the scripts path.
Geckodriver is designed to drive gecko-based web browser, like Mozilla Firefox.

Download the appropriate geckodriver based on your platform from below download page
Download Page: https://github.com/mozilla/geckodriver/releases
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from random import choice

drivers = webdriver.Firefox()
drivers.get("http://www.practiceselenium.com/practice-form.html")
before_form_submit = drivers.title
print(before_form_submit)

data = {
    'fname':"Suhas",
    'lname':"Manjunath",
    'sex': "sex-0",
    'years':[1,2,3,4,5,6,7],
    'date':datetime.now(),
    'fav':['BlackTea','RedTea','oolongtea'],
    'exicting': ['tool-0','tool-1','tool-2']
   }

def form_submit(form_data):
    firstname = drivers.find_element_by_name("firstname")
    firstname.send_keys(data['fname'])
    lastname = drivers.find_element_by_name("lastname")
    lastname.send_keys(data['lname'])
    if data['sex']=='sex-0':
        sex = drivers.find_elements_by_xpath("//input[@type='radio' and @value='Male']")[0]
    elif data['sex']=='sex-1':
        sex = drivers.find_elements_by_xpath("//input[@type='radio' and @value='Female']")[0]  
    sex.click()
    years = drivers.find_elements_by_xpath("//input[@type='radio' and @name='exp' and @value=" + str(choice(data['years'])) + ']')[0]
    years.click()
    date = drivers.find_element_by_id("datepicker")
    date.send_keys(str(data['date']))
    fav_chai = choice(data['fav'])
    if (fav_chai=='BlackTea'):
        chai = drivers.find_elements_by_xpath("//input[@type='checkbox' and @value='Black Tea']")[0]
    elif(fav_chai=='RedTea'):
        chai = drivers.find_elements_by_xpath("//input[@type='checkbox' and @value='Red Tea']")[0]
    elif(fav_chai=='oolongtea'):
        chai = drivers.find_elements_by_xpath("//input[@type='checkbox' and @value='oolong tea']")[0]
    chai.click()
    myChoice = choice(data['exicting'])
    if(myChoice=='tool-0'):
        exicting = drivers.find_elements_by_xpath("//input[@type='checkbox' and @value='Break']")[0]
    elif(myChoice=='tool-1'):
        exicting = drivers.find_elements_by_xpath("//input[@type='checkbox' and @value='Harmless Addiction']")[0]
    else:
        exicting = drivers.find_elements_by_xpath("//input[@type='checkbox' and @value='One of those things']")[0]
    exicting.click()
    elem_by_tag_option = drivers.find_elements_by_tag_name("option")
    continents = elem_by_tag_option[0:7]
    choice(continents).click()
    commands = elem_by_tag_option[7:]
    choice(commands).click()
    button = drivers.find_element_by_xpath("//button[@id='submit']")
    button.click()
    after_form_submit = drivers.title
    print("\n" + after_form_submit)
    if(after_form_submit==("Welcome" or "Home")):
        print("\nForm was successfully submitted and the home page was loaded!!!!")
        time.sleep(10)
        drivers.quit()
        
form_submit(data)

