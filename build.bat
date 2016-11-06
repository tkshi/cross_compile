git pull
rmdir /s /q dist
rmdir /s /q build
copy chromedriver.exe dist¥main
pyinstaller main.py --noconsole