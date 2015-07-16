#!/usr/bin/python
#coding:utf-8
from PyQt4.QtCore import *  
from PyQt4.QtGui import *  
import sys  

# 和位置计算相关的函数 
class Geometry(QDialog):  
    def __init__(self, parent = None):  
        super(Geometry, self).__init__(parent)  
  
        self.setWindowTitle("Geometry")  
  
        Label1 = QLabel("x0:")  
        Label2 = QLabel("y0:")  
        Label3 = QLabel("frameGeometry():")  
        Label4 = QLabel("pos():")  
        Label5 = QLabel("geometry():")  
        Label6 = QLabel("width():")  
        Label7 = QLabel("height():")  
        Label8 = QLabel("rect():")  
        Label9 = QLabel("size():")  
          
        self.xLabel = QLabel()  
        self.yLabel = QLabel()  
        self.frameGeoLabel = QLabel()  
        self.posLabel = QLabel()  
        self.geoLabel = QLabel()  
        self.widthLabel = QLabel()  
        self.heightLabel = QLabel()  
        self.rectLabel = QLabel()  
        self.sizeLabel = QLabel()  
  
        layout = QGridLayout()  
        layout.addWidget(Label1, 0, 0)  
        layout.addWidget(self.xLabel, 0, 1)  
        layout.addWidget(Label2, 1, 0)  
        layout.addWidget(self.yLabel, 1, 1)  
        layout.addWidget(Label3, 2, 0)  
        layout.addWidget(self.frameGeoLabel, 2, 1)  
        layout.addWidget(Label4, 3, 0)  
        layout.addWidget(self.posLabel, 3, 1)  
        layout.addWidget(Label5, 4, 0)  
        layout.addWidget(self.geoLabel, 4, 1)  
        layout.addWidget(Label6, 5, 0)  
        layout.addWidget(self.widthLabel, 5, 1)  
        layout.addWidget(Label7, 6, 0)  
        layout.addWidget(self.heightLabel, 6, 1)  
        layout.addWidget(Label8, 7, 0)  
        layout.addWidget(self.rectLabel, 7, 1)  
        layout.addWidget(Label9, 8, 0)  
        layout.addWidget(self.sizeLabel, 8, 1)  
  
        self.setLayout(layout)  
  
        self.updateLabel()  
  
    def moveEvent(self,event):  
        self.updateLabel()  
  
    def resizeEvent(self,event):  
        self.updateLabel()  
  
    def updateLabel(self):  
        temp = QString()  
  
        self.xLabel.setText(temp.setNum(self.x()))  
        self.yLabel.setText(temp.setNum(self.y()))  
        self.frameGeoLabel.setText(temp.setNum(self.frameGeometry().x()) + "," + temp.setNum(self.frameGeometry().y()) + "," + temp.setNum(self.frameGeometry().width()) + "," + temp.setNum(self.frameGeometry().height()))  
  
        self.posLabel.setText(temp.setNum(self.pos().x()) + "," + temp.setNum(self.pos().y()))  
        self.geoLabel.setText(temp.setNum(self.geometry().x()) + "," + temp.setNum(self.geometry().y()) + "," + temp.setNum(self.geometry().width()) + "," + temp.setNum(self.geometry().height()))  
        self.widthLabel.setText(temp.setNum(self.width()))  
        self.heightLabel.setText(temp.setNum(self.height()))  
        self.rectLabel.setText(temp.setNum(self.rect().x()) + "," + temp.setNum(self.rect().y()) + "," + temp.setNum(self.rect().width()) + "," + temp.setNum(self.rect().height()))  
        self.sizeLabel.setText(temp.setNum(self.size().width()) + "," + temp.setNum(self.size().height()))  
  
          
app = QApplication(sys.argv)  
form = Geometry()  
form.show()  
app.exec_()  