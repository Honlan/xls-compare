#!/usr/bin/python
#coding:utf-8
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# 一个最简单的Hello World程序
app = QApplication(sys.argv)
b = QPushButton('Hello World!')
b.show()
app.connect(b, SIGNAL('clicked()'), app, SLOT('quit()'))
app.exec_()