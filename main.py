import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import platform
if  platform.system() == 'Windows':
	CHROMEDRIVER_PATH = "./chromedriver.exe"
else:
	CHROMEDRIVER_PATH = "./chromedriver"

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	driver = webdriver.Chrome(CHROMEDRIVER_PATH)
	driver.get("http://www.python.org")
	assert "Python" in driver.title
	elem = driver.find_element_by_name("q")
	elem.clear()
	elem.send_keys("pycon")
	elem.send_keys(Keys.RETURN)
	assert "No results found." not in driver.page_source
	driver.close()
	return "Hello World!"

if __name__ == "__main__":
	webbrowser.open('http://127.0.0.1:5000/')
	app.run()