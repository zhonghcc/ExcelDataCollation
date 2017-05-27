# -*- coding: utf-8 -*-

import os
import xlrd
import xlwt
import logging
import json
import filter.repeat

BASE_PATH = "config/"
class DataCollator():

    def __init__(self):
        self.logger = logging.getLogger("DataCollation.DataCollator")

    def process(self,path,config,callback,complete):
        self.logger.info("path="+path)
        self.logger.info("config="+config)

        ### read config file and init filters
        configObj = self.getConfigContent(config)
        self.resultColumn = self.convertLetterToNum(configObj["output"])
        self.filterName = configObj["name"]
        self.filters = []
        for filterObj in configObj["filters"]:
            filter = object()
            filter.source = self.convertLetterToNum(filterObj["source"])
            filter.name = filterObj["name"]
            filter.processor = filter.repeat.Repeat()


        ### read and deal with xls
        data = xlrd.open_workbook(path)
        table = data.sheets()[0] # TODO to process only the first sheet
        nrows = table.nrows
        for i in range(nrows ):
            print table.row_values(i)[0]
        pass

    def stop(self):
        pass

    def getConfigList(self):
        arr = os.listdir(BASE_PATH)
        self.logger.info(arr)
        configList = []
        for fileName in arr:
            fullPath = BASE_PATH + fileName
            if os.path.isfile(fullPath):
                configName,ext = os.path.splitext(fileName)
                configList.append(configName)
        self.logger.info(configList)
        return configList

    def getConfigContent(self,configName):
        file = open(BASE_PATH+configName+".json")
        try:
            content = file.read()
            # print content
            obj = json.loads(content)
            print obj
            return obj
        finally:
            file.close()

    def convertLetterToNum(self,str):
        str = str.upper()
        lenStr = len(str)
        ordA = ord('A')
        total = 0
        for ch in str:
            ordCh = ord(ch)
            if ordCh>ord('Z') or ordCh<ord('A'):
                return "Error:"+str
            total = total*26
            total = total + ord(ch)-ordA +1
        print total

def mainComplete():
    print "Complete"

def mainCallback(index,length):
    print index,length

if __name__ == '__main__':
    collator = DataCollator()
    collator.convertLetterToNum('A')
    collator.convertLetterToNum('B')
    collator.convertLetterToNum('DF')
    collator.process("../example/1.xlsx","repeat",mainCallback,mainComplete)
