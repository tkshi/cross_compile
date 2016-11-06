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

from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello():
	# driver = webdriver.Chrome(CHROMEDRIVER_PATH)
	# driver.get("http://www.python.org")
	# assert "Python" in driver.title
	# elem = driver.find_element_by_name("q")
	# elem.clear()
	# elem.send_keys("pycon")
	# elem.send_keys(Keys.RETURN)
	# assert "No results found." not in driver.page_source
	# driver.close()
	return "Hello World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "success"

if __name__ == "__main__":
	webbrowser.open('http://127.0.0.1:5000/')
	app.run()