#!/usr/bin/python
#coding:utf-8
from PyQt4.QtCore import *  
from PyQt4.QtGui import *  
import sys  

# 常见布局的使用
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
  
class LayoutDialog(QDialog):  
    def __init__(self,parent=None):  
        super(LayoutDialog,self).__init__(parent)  
        self.setWindowTitle(self.tr("用户信息"))  
          
        label1 = QLabel(self.tr("用户名:"))  
        label2 = QLabel(self.tr("姓名："))  
        label3 = QLabel(self.tr("性别:"))  
        label4 = QLabel(self.tr("部门:"))  
        label5 = QLabel(self.tr("年龄:"))  
        otherLabel = QLabel(self.tr("备注:"))  
        otherLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)  
        userLineEdit = QLineEdit()  
        nameLineEdit = QLineEdit()  
        sexComboBox = QComboBox()  
        sexComboBox.insertItem(0,self.tr("男"))  
        sexComboBox.insertItem(1,self.tr("女"))  
        departmentTextEdit = QTextEdit()  
        ageLineEdit = QLineEdit()  
  
        labelCol = 0  
        contentCol = 1  
  
        leftLayout = QGridLayout()  
        leftLayout.addWidget(label1, 0, labelCol)  
        leftLayout.addWidget(userLineEdit, 0, contentCol)  
        leftLayout.addWidget(label2, 1, labelCol)  
        leftLayout.addWidget(nameLineEdit, 1, contentCol)  
        leftLayout.addWidget(label3, 2, labelCol)  
        leftLayout.addWidget(sexComboBox, 2, contentCol)  
        leftLayout.addWidget(label4, 3, labelCol)  
        leftLayout.addWidget(departmentTextEdit, 3, contentCol)  
        leftLayout.addWidget(label5, 4, labelCol)  
        leftLayout.addWidget(ageLineEdit, 4, contentCol)  
        leftLayout.addWidget(otherLabel, 5, labelCol, 1, 2)  
        leftLayout.setColumnStretch(0, 1)  
        leftLayout.setColumnStretch(1, 3)  
  
        label6 = QLabel(self.tr("头像:"))  
        iconLabel = QLabel()  
        icon = QPixmap("image/2.jpg")  
        iconLabel.setPixmap(icon)  
        iconLabel.resize(icon.width(),icon.height())  
        iconPushButton = QPushButton(self.tr("改变"))  
        hLayout = QHBoxLayout()  
        hLayout.setSpacing(20)  
        hLayout.addWidget(label6)  
        hLayout.addWidget(iconLabel)  
        hLayout.addWidget(iconPushButton)  
  
        label7 = QLabel(self.tr("个人说明:"))  
        descTextEdit = QTextEdit()  
  
        rightLayout = QVBoxLayout()  
        rightLayout.setMargin(10)  
        rightLayout.addLayout(hLayout)  
        rightLayout.addWidget(label7)  
        rightLayout.addWidget(descTextEdit)  
  
        OKPushButton = QPushButton(self.tr("确定"))  
        cancelPushButton = QPushButton(self.tr("取消"))  
        bottomLayout = QHBoxLayout()  
        bottomLayout.addStretch()  
        bottomLayout.addWidget(OKPushButton)  
        bottomLayout.addWidget(cancelPushButton)  
  
        mainLayout = QGridLayout(self)  
        mainLayout.setMargin(15)  
        mainLayout.setSpacing(10)  
        mainLayout.addLayout(leftLayout, 0, 0)  
        mainLayout.addLayout(rightLayout, 0, 1)  
        mainLayout.addLayout(bottomLayout, 1, 0, 1, 2)  
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)  
   
app = QApplication(sys.argv)  
dialog = LayoutDialog()  
dialog.show()  
app.exec_()  