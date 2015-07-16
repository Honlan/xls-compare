#!/usr/bin/python
#coding:utf-8
from PyQt4.QtCore import *  
from PyQt4.QtGui import *  
import sys  

# 使用Palette改变控件样式
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
  
class Palette(QDialog):  
    def __init__(self,parent=None):  
        super(Palette,self).__init__(parent)  
        self.setWindowTitle(self.tr("QPalette对话框"))  
  
        mainLayout = QHBoxLayout(self)  
        self.ctrlFrame = QFrame()  
        self.contentFrame = QFrame()  
        self.contentFrame.setAutoFillBackground(True)  
        self.createCtrlFrame()  
        self.createContentFrame()  
        mainLayout.addWidget(self.ctrlFrame)  
        mainLayout.addWidget(self.contentFrame)          
  
    def createCtrlFrame(self):  
        label1 = QLabel("QPalette.Window")  
        self.windowComboBox = QComboBox()  
        label2 = QLabel("QPalette.WindowText")  
        self.windowTextComboBox = QComboBox()  
        label3 = QLabel("QPalette.Button")  
        self.buttonComboBox = QComboBox()  
        label4 = QLabel("QPalette.ButtonText")  
        self.buttonTextComboBox = QComboBox()  
        label5 = QLabel("QPalette.Base")  
        self.baseComboBox = QComboBox()  
  
        self.fillColorList(self.windowComboBox)  
        self.fillColorList(self.windowTextComboBox)  
        self.fillColorList(self.buttonComboBox)  
        self.fillColorList(self.buttonTextComboBox)  
        self.fillColorList(self.baseComboBox)  
        self.connect(self.windowComboBox, SIGNAL("currentIndexChanged(int)"), self.slotWindow)  
        self.connect(self.windowTextComboBox, SIGNAL("currentIndexChanged(int)"), self.slotWindowText)  
        self.connect(self.buttonComboBox, SIGNAL("currentIndexChanged(int)"), self.slotButton)  
        self.connect(self.buttonTextComboBox, SIGNAL("currentIndexChanged(int)"), self.slotButtonText)  
        self.connect(self.baseComboBox, SIGNAL("currentIndexChanged(int)"), self.slotBase)  
          
        gridLayout = QGridLayout()  
        gridLayout.addWidget(label1, 0, 0)  
        gridLayout.addWidget(self.windowComboBox, 0, 1)  
        gridLayout.addWidget(label2, 1, 0)  
        gridLayout.addWidget(self.windowTextComboBox, 1, 1)  
        gridLayout.addWidget(label3, 2, 0)  
        gridLayout.addWidget(self.buttonComboBox, 2, 1)  
        gridLayout.addWidget(label4, 3, 0)  
        gridLayout.addWidget(self.buttonTextComboBox, 3, 1)  
        gridLayout.addWidget(label5, 4, 0)  
        gridLayout.addWidget(self.baseComboBox)  
  
        self.ctrlFrame.setLayout(gridLayout)  
  
    def fillColorList(self,comboBox):  
        colorList = QColor.colorNames()  
          
        for color in colorList:  
            pix = QPixmap(QSize(70, 20))  
            pix.fill(QColor(color))  
            comboBox.addItem(QIcon(pix), color)  
            comboBox.setIconSize(QSize(70, 20))  
            comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)  
          
    def createContentFrame(self):  
        label1 = QLabel(self.tr("请选择一个值"))  
        valueComboBox = QComboBox()  
        valueComboBox.addItem("1")  
        valueComboBox.addItem("2")  
        label2 = QLabel(self.tr("请输入字符串"))  
        stringLineEdit = QLineEdit()  
        textEditText = QTextEdit(self.tr("请输入"))  
        hLayout = QHBoxLayout()  
        okButton = QPushButton(self.tr("确定"))  
        cancelButton = QPushButton(self.tr("取消"))  
        hLayout.addStretch()  
        hLayout.addWidget(okButton)  
        hLayout.addWidget(cancelButton)  
        gridLayout = QGridLayout()  
        gridLayout.addWidget(label1, 0, 0)  
        gridLayout.addWidget(valueComboBox, 0, 1)  
        gridLayout.addWidget(label2, 1, 0)  
        gridLayout.addWidget(stringLineEdit, 1, 1)  
        gridLayout.addWidget(textEditText, 2, 0, 1, 2)  
        gridLayout.addLayout(hLayout, 3, 0, 1, 2)  
        self.contentFrame.setLayout(gridLayout)  
  
    def slotWindow(self):  
        colorList = QColor.colorNames()  
        color = QColor(colorList[self.windowComboBox.currentIndex()])  
        p = self.contentFrame.palette()  
        p.setColor(QPalette.Window, color)  
        self.contentFrame.setPalette(p)  
  
    def slotWindowText(self):  
        colorList = QColor.colorNames()  
        color = QColor(colorList[self.windowTextComboBox.currentIndex()])  
        p = self.contentFrame.palette()  
        p.setColor(QPalette.WindowText, color)  
        self.contentFrame.setPalette(p)  
  
    def slotButton(self):  
        colorList = QColor.colorNames()  
        color = QColor(colorList[self.buttonComboBox.currentIndex()])  
        p = self.contentFrame.palette()  
        p.setColor(QPalette.Button, color)  
        self.contentFrame.setPalette(p)  
  
    def slotButtonText(self):  
        colorList = QColor.colorNames()  
        color = QColor(colorList[self.buttonTextComboBox.currentIndex()])  
        p = self.contentFrame.palette()  
        p.setColor(QPalette.ButtonText, color)  
        self.contentFrame.setPalette(p)  
  
    def slotBase(self):  
        colorList = QColor.colorNames()  
        color = QColor(colorList[self.baseComboBox.currentIndex()])  
        p = self.contentFrame.palette()  
        p.setColor(QPalette.Base, color)  
        self.contentFrame.setPalette(p)  
  
app = QApplication(sys.argv)  
main = Palette()  
main.show()  
app.exec_()  