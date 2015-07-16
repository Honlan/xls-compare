#!/usr/bin/python
#coding:utf-8
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# 表格的实现
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
   
class MyTable(QTableWidget):  
    def __init__(self,parent=None):  
        super(MyTable,self).__init__(parent)  
        self.setColumnCount(5)  
        self.setRowCount(2)  
        self.setItem(0, 0, QTableWidgetItem(self.tr("性别")))  
        self.setItem(0, 1, QTableWidgetItem(self.tr("姓名")))  
        self.setItem(0, 2, QTableWidgetItem(self.tr("出生日期")))  
        self.setItem(0, 3, QTableWidgetItem(self.tr("职业")))  
        self.setItem(0, 4, QTableWidgetItem(self.tr("收入")))  
        lbp1 = QLabel()  
        lbp1.setPixmap(QPixmap("image/4.gif"))  
        self.setCellWidget(1, 0, lbp1)  
        twi1 = QTableWidgetItem("Tom")  
        self.setItem(1, 1, twi1)  
        dte1 = QDateTimeEdit()  
        dte1.setDateTime(QDateTime.currentDateTime())  
        dte1.setDisplayFormat("yyyy/mm/dd")  
        dte1.setCalendarPopup(True)  
        self.setCellWidget(1, 2, dte1)  
        cbw = QComboBox()  
        cbw.addItem("Worker")  
        cbw.addItem("Famer")  
        cbw.addItem("Doctor")  
        cbw.addItem("Lawyer")  
        cbw.addItem("Soldier")  
        self.setCellWidget(1, 3, cbw)  
        sb1 = QSpinBox()  
        sb1.setRange(1000, 10000)  
        self.setCellWidget(1, 4, sb1)  
    
app = QApplication(sys.argv)  
myqq = MyTable()  
myqq.setWindowTitle("My Table")  
myqq.show()  
app.exec_()  