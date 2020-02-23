#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--window-size=1920x1080")

driver = webdriver.Firefox(options=firefox_options)
driver.get("YOUR_FORM_LINK")
elem = driver.find_elements_by_class_name("freebirdThemedRadio")

def nuke(driver, elem, count):
    ctr = 0
    for i in range (0, count): 
        driver.get("YOUR_FORM_LINK")
        elem = driver.find_elements_by_class_name("freebirdThemedRadio")

        bias = 0
        if ctr >= 7 and ctr < 9:
            bias = 1
        elif ctr >= 9:
            bias = 2
        for i in range (0, len(elem)):
            if (i%3 == bias):
                elem[i].click()
        el=driver.find_elements_by_class_name("exportButtonContent")
        el[0].click()
        ctr += 1
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

count=10
nuke(driver, elem, count)

print("Succeeded!")
driver.close()
