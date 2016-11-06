import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import platform
if  platform.system() == 'Windows':
	CHROMEDRIVER_PATH = "./chromedriver.exe"
else:
	CHROMEDRIVER_PATH = "./chromedriver"

driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()