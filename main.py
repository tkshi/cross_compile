#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform

def startWebKit():
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

class MainMenu(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self, parent=parent)
		self.setGeometry(10,10,40,300)
		button = QtGui.QPushButton('start',self)
		self.Label = QtGui.QLabel('',self)
		self.Label.setGeometry(20,20,40,40)
		self.connect(button,QtCore.SIGNAL('clicked()'),self.changeText)

	def changeText(self):
		startWebKit()
		self.Label.setText("abcd")


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
              
        exitGUI=QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
        exitAction = QAction(exitGUI, '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        qtInfoGUI=QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        qtInfoAction = QAction(qtInfoGUI, '&AboutQt', self)        
        qtInfoAction.setShortcut('Ctrl+I')
        qtInfoAction.setStatusTip('Show Qt info')
        qtInfoAction.triggered.connect(qApp.aboutQt)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Info')
        fileMenu.addAction(qtInfoAction)
        fileMenu.addAction(exitAction)
        menubar.setNativeMenuBar(False) #for mac

        main = MainMenu()
        self.setCentralWidget(main)        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('TwitterAutoRegisterTool')    
        self.show()
        # startWebKit()
        
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()   