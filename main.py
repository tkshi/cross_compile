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
from Error import *



#coding=utf-8
import sys
from PyQt4 import QtGui, QtCore
from Runner import start
class Window( QtGui.QWidget ):
    def __init__( self ):
        super( Window, self ).__init__()
        self.setWindowTitle( "TwitterAutoRegister_ver0.5" )
        self.resize( 500, 800 )

        gridlayout = QtGui.QGridLayout()

        self.tryCount = QtGui.QLineEdit()
        self.tryCount.setPlaceholderText(u"twitter登録回数 例) 10")
        gridlayout.addWidget( self.tryCount )

        self.phoneTryCount = QtGui.QLineEdit()
        self.phoneTryCount.setPlaceholderText(u"電話の登録回数 例) 5")
        gridlayout.addWidget( self.phoneTryCount )

        self.ipAdressForm = QtGui.QLineEdit()
        self.ipAdressForm.setPlaceholderText(u"TwitterでソーシャルログインするIPアドレス 例) 36.55.241.31")
        gridlayout.addWidget( self.ipAdressForm )


        self.twitterPathForm = QtGui.QLineEdit()
        self.twitterPathForm.setPlaceholderText(u"C¥documents¥twitter.xls")
        gridlayout.addWidget( self.twitterPathForm )
        button2 = QtGui.QPushButton( u"Twitterファイルを選択" )
        gridlayout.addWidget( button2 ,3,1)
        self.connect( button2, QtCore.SIGNAL( 'clicked()' ), self.twitterFileOpen )

        self.googlePathForm = QtGui.QLineEdit()
        self.googlePathForm.setPlaceholderText(u"C¥documents¥google.xls")
        gridlayout.addWidget( self.googlePathForm )
        button2 = QtGui.QPushButton( u"Googleファイルを選択" )
        gridlayout.addWidget( button2 )
        self.connect( button2, QtCore.SIGNAL( 'clicked()' ), self.googleFileOpen )

        button2 = QtGui.QPushButton( "Start" )
        gridlayout.addWidget( button2 )
        self.connect( button2, QtCore.SIGNAL( 'clicked()' ), self.startWebKit )

        self.Label = QtGui.QLabel('')
        gridlayout.addWidget( self.Label )

        self.setLayout( gridlayout )
    def twitterFileOpen(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        self.twitter_excel_path = fileName
        self.twitterPathForm.setText(self.twitter_excel_path)

    def googleFileOpen(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        self.google_excel_path = fileName
        self.googlePathForm.setText(self.google_excel_path)

    def startWebKit(self):
        APP_IP = str(self.ipAdressForm.text())
        try_count = int(self.tryCount.text())
        phone_try_count = int(self.phoneTryCount.text())



        try:
            start(APP_IP=APP_IP,TWITTER_SHEET_PATH=self.twitter_excel_path,GOOGLE_SHEET_PATH=self.google_excel_path,TRY_COUNT=try_count,PHONE_TRY_COUNT=phone_try_count)
        except OverTryCountError:
            self.Label.setText(u"登録完了です")
app = QtGui.QApplication( sys.argv )
window = Window()
window.show()
app.exec_()
