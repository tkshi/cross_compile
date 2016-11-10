#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../xml')
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
from main import start
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
        # self.connect( button2, QtCore.SIGNAL( 'clicked()' ), self.fileOpen )
        self.setLayout( gridlayout )
    def fileOpen(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        print(fileName)
    def startWebKit(self):
        start()
app = QtGui.QApplication( sys.argv )
window = Window()
window.show()
app.exec_()
