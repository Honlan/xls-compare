#!/usr/bin/python
#coding:utf-8
from PyQt4.QtCore import *  
from PyQt4.QtGui import *  
import sys  

# 多窗口的实现
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
  
class MainWidget(QMainWindow):  
    def __init__(self, parent = None):  
        super(MainWidget,self).__init__(parent)  
        self.setWindowTitle(self.tr("多文档窗口"))  
        self.workSpace = QWorkspace()  
        self.setCentralWidget(self.workSpace)  
  
        window1 = QMainWindow()  
        window1.setWindowTitle(self.tr("窗口1"))  
        edit1 = QTextEdit(self.tr("子窗口1"))  
        window1.setCentralWidget(edit1)  
        window2 = QMainWindow()  
        window2.setWindowTitle(self.tr("窗口2"))  
        edit2 = QTextEdit(self.tr("子窗口2"))  
        window2.setCentralWidget(edit2)  
        window3 = QMainWindow()  
        window3.setWindowTitle(self.tr("窗口3"))  
        edit3 = QTextEdit(self.tr("子窗口3"))  
        window3.setCentralWidget(edit3)  
  
        self.workSpace.addWindow(window1)  
        self.workSpace.addWindow(window2)  
        self.workSpace.addWindow(window3)  
          
        self.createMenu()  
        self.slotScroll()  
          
    def createMenu(self):  
        layoutMenu = self.menuBar().addMenu(self.tr("布局"))  
        arrange = QAction(self.tr("排列图标"), self)  
        self.connect(arrange, SIGNAL("triggered()"), self.workSpace, SLOT("arrangeIcons()"))  
        layoutMenu.addAction(arrange)  
  
        tile = QAction(self.tr("平铺"), self)  
        self.connect(tile, SIGNAL("triggered()"), self.workSpace, SLOT("tile()"))  
        layoutMenu.addAction(tile)  
  
        cascade = QAction(self.tr("层叠"), self)  
        self.connect(cascade, SIGNAL("triggered()"), self.workSpace, SLOT("cascade()"))  
        layoutMenu.addAction(cascade)  
  
        otherMenu = self.menuBar().addMenu(self.tr("其它"))  
        scrollAct = QAction(self.tr("滚动"), self)  
        self.connect(scrollAct, SIGNAL("triggered()"), self.slotScroll)  
        otherMenu.addAction(scrollAct)  
        otherMenu.addSeparator()  
  
        nextAct = QAction(self.tr("下一个"), self)  
        self.connect(nextAct, SIGNAL("triggered()"), self.workSpace, SLOT("activateNextWindow()"))  
        otherMenu.addAction(nextAct)  
  
        previousAct = QAction(self.tr("上一个"), self)  
        self.connect(previousAct, SIGNAL("triggered()"), self.workSpace, SLOT("activatePreviousWindow()"))  
        otherMenu.addAction(previousAct)  
  
    def slotScroll(self):  
        self.workSpace.setScrollBarsEnabled(not self.workSpace.scrollBarsEnabled())  
          
app = QApplication(sys.argv)  
main = MainWidget()  
main.show()  
app.exec_()  