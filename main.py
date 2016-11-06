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



#coding=utf-8
import sys
from PyQt4 import QtGui, QtCore
class Window( QtGui.QWidget ):
    def __init__( self ):
        super( Window, self ).__init__()
        self.setWindowTitle( "TwitterAutoRegister" )
        self.resize( 500, 200 )
         
        gridlayout = QtGui.QGridLayout()
         
        button2 = QtGui.QPushButton( "Start" )
         
        self.textFile = QtGui.QLineEdit()
        self.textFile.setText( "https://twitter.com/?lang=ja" )

        gridlayout.addWidget( self.textFile )
        gridlayout.addWidget( button2, 1, 1, 1, 3 )
        self.connect( button2, QtCore.SIGNAL( 'clicked()' ), self.startWebKit )
        self.setLayout( gridlayout )
    def startWebKit(self):
        url = self.textFile.text()
        print(type(str(url)))
        if  platform.system() == 'Windows':
            CHROMEDRIVER_PATH = "./chromedriver.exe"
        else:
            CHROMEDRIVER_PATH = "./chromedriver"

        driver = webdriver.Chrome(CHROMEDRIVER_PATH)
        driver.get(str(url))
        driver.close() 
app = QtGui.QApplication( sys.argv )
window = Window()
window.show()
app.exec_()