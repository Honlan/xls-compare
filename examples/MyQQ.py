#!/usr/bin/python
#coding:utf-8
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

# 类QQ布局实现
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
  
class MyQQ(QToolBox):  
    def __init__(self,parent=None):  
        super(MyQQ,self).__init__(parent)  
          
        toolButton1_1 = QToolButton()  
        toolButton1_1.setText(self.tr("朽木"))  
        toolButton1_1.setIcon(QIcon("image/9.gif"))  
        toolButton1_1.setIconSize(QSize(60,60))  
        toolButton1_1.setAutoRaise(True)  
        toolButton1_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton1_2 = QToolButton()  
        toolButton1_2.setText(self.tr("Cindy"))  
        toolButton1_2.setIcon(QIcon("image/8.gif"))  
        toolButton1_2.setIconSize(QSize(60,60))  
        toolButton1_2.setAutoRaise(True)  
        toolButton1_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton1_3 = QToolButton()  
        toolButton1_3.setText(self.tr("了了"))  
        toolButton1_3.setIcon(QIcon("image/1.gif"))  
        toolButton1_3.setIconSize(QSize(60,60))  
        toolButton1_3.setAutoRaise(True)  
        toolButton1_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton1_4 = QToolButton()  
        toolButton1_4.setText(self.tr("张三虎"))  
        toolButton1_4.setIcon(QIcon("image/3.gif"))  
        toolButton1_4.setIconSize(QSize(60,60))  
        toolButton1_4.setAutoRaise(True)  
        toolButton1_4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton1_5 = QToolButton()  
        toolButton1_5.setText(self.tr("CSDN"))  
        toolButton1_5.setIcon(QIcon("image/4.gif"))  
        toolButton1_5.setIconSize(QSize(60,60))  
        toolButton1_5.setAutoRaise(True)  
        toolButton1_5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton2_1 = QToolButton()  
        toolButton2_1.setText(self.tr("天的另一边"))  
        toolButton2_1.setIcon(QIcon("image/5.gif"))  
        toolButton2_1.setIconSize(QSize(60,60))  
        toolButton2_1.setAutoRaise(True)  
        toolButton2_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton2_2 = QToolButton()  
        toolButton2_2.setText(self.tr("蓝绿不分"))  
        toolButton2_2.setIcon(QIcon("image/6.gif"))  
        toolButton2_2.setIconSize(QSize(60,60))  
        toolButton2_2.setAutoRaise(True)  
        toolButton2_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton3_1 = QToolButton()  
        toolButton3_1.setText(self.tr("老牛"))  
        toolButton3_1.setIcon(QIcon("image/7.gif"))  
        toolButton3_1.setIconSize(QSize(60,60))  
        toolButton3_1.setAutoRaise(True)  
        toolButton3_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton3_2 = QToolButton()  
        toolButton3_2.setText(self.tr("张三疯"))  
        toolButton3_2.setIcon(QIcon("image/8.gif"))  
        toolButton3_2.setIconSize(QSize(60,60))  
        toolButton3_2.setAutoRaise(True)  
        toolButton3_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        groupbox1 = QGroupBox()  
        vlayout1 = QVBoxLayout(groupbox1)  
        vlayout1.setMargin(10)  
        vlayout1.setAlignment(Qt.AlignCenter)  
        vlayout1.addWidget(toolButton1_1)  
        vlayout1.addWidget(toolButton1_2)  
        vlayout1.addWidget(toolButton1_3)  
        vlayout1.addWidget(toolButton1_4)  
        vlayout1.addWidget(toolButton1_5)  
        vlayout1.addStretch()  
  
        groupbox2 = QGroupBox()  
        vlayout2 = QVBoxLayout(groupbox2)  
        vlayout2.setMargin(10)  
        vlayout2.setAlignment(Qt.AlignCenter)  
        vlayout2.addWidget(toolButton2_1)  
        vlayout2.addWidget(toolButton2_2)  
           
        groupbox3 = QGroupBox()  
        vlayout3 = QVBoxLayout(groupbox3)  
        vlayout3.setMargin(10)  
        vlayout3.setAlignment(Qt.AlignCenter)  
        vlayout3.addWidget(toolButton3_1)  
        vlayout3.addWidget(toolButton3_2)  
  
        self.addItem(groupbox1,self.tr("我的好友"))  
        self.addItem(groupbox2,self.tr("同事"))  
        self.addItem(groupbox3,self.tr("黑名单"))  
  
app = QApplication(sys.argv)  
myqq = MyQQ()  
myqq.setWindowTitle("My QQ")  
myqq.show()  
app.exec_()  