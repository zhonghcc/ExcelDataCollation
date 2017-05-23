#coding=utf-8 
'''
Created on 2015年12月25日

@author: zhonghcc
'''
import dataCollator
from PyQt4 import QtGui,uic,QtCore
import logging
import chardet
from PyQt4.QtGui import QMessageBox,QFileDialog
READY,SENDING,SENDIING_COMPLETED = range(3) #state enum
class MainWindow(QtGui.QMainWindow):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        '''
        Constructor
        '''
        self.logger = logging.getLogger("DataCollation.MainWindow")
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("resources/mainwindow.ui", self)

        self.progressBar.setMinimum(1)
        self.progressBar.setMaximum(100)

        self.dataCollator = dataCollator.DataCollator()
        arr = self.dataCollator.getConfigList();
        for config in arr:
            self.ui.cb_config.addItem(unicode(config.decode("GBK")))
        self.show()
        
    def start(self):
        trigger = QtCore.SIGNAL("triggered()")
        click = QtCore.SIGNAL("clicked()")
        self.connect(self.ui.btn_open, click,self.openFileChoseDialog)
        self.connect(self.ui.btn_start, click,self.processData)
        

        
    def openFileChoseDialog(self):
        self.logger.debug('opening FileChoseDialog')
        filename=QFileDialog.getOpenFileName(self,"Open file dialog","/","Excel file(*.xls|*.xlxs)")
        if filename == '': return
        self.fileName.setText(filename) 
        
    

            
    def displayProcess(self,index,length):
        
        if(index > 0 and length > 1):
            status = index*1.00/(length-1)*100
            print status
            self.progressBar.setValue(status)
            
    def processData(self):
        if not (self.state == LOADING_COMPLETED or self.state == SENDING):
            message = u'当前没有要发送的数据，请选择要处理的文件并点击\'数据准备\'按钮'
            self.showMessage(message)
            return
        
        if self.state == SENDING:
            message = u'您确认要取消吗？'
            if self.confirmMessage(message):
                self.sender.stopWork()
                self.state=LOADING_COMPLETED
            return
        
        
        self.state = SENDING
        self.sender.sendData(self.spb_inteval.value(), self.displayProcess , self.sendComplete)
            
            
    
    
    def sendComplete(self):
        self.state = SENDIING_COMPLETED
   
    def showMessage(self,message):
        msgBox = QMessageBox.information(None,u'提示',message)
#         msgBox.exec_()
    def confirmMessage(self,message):
        result = QMessageBox.question(None,u'请确认',message,QMessageBox.Yes|QMessageBox.No)
        if result == QMessageBox.Yes:
            return True
        else:
            return False
    
