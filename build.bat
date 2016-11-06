git pull
rmdir /s /q dist
rmdir /s /q build
copy dist¥main¥main.exe main.exe
pyinstaller main.py --noconsole