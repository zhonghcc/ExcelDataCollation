# -*- coding: utf-8 -*-

import os
import xlrd
import xlwt
import xlutils.copy
import logging
import logging.config
import json
from filter import filtersClass
from filter import repeat,idcard,mobileLocate

BASE_PATH = "config/"
class DataCollator():

    def __init__(self):
        self.logger = logging.getLogger("DataCollation.DataCollator")

    def initFilters(self,config):
        ### read config file and init filters
        configObj = self.getConfigContent(config)
        self.resultColumn = self.convertLetterToNum(configObj["output"])
        self.filterName = configObj["name"]
        self.filters = []

        class FilterObj(): #inner cls
            def __init__(self):
                pass
        for filterObj in configObj["filters"]:
            filter = FilterObj()
            filter.source = self.convertLetterToNum(filterObj["source"])
            filter.name = filterObj["name"]
            filter.processor = filtersClass[filter.name]() #instance
            strTarget = None
            if filterObj.has_key("target"):
                strTarget = filterObj["target"]
            filter.target = []
            if strTarget is not None:
                arrTarget = strTarget.split(',')
                for tar in arrTarget:
                    if tar == '':
                        targetNum = -1
                    else:
                        targetNum = self.convertLetterToNum(tar)
                    filter.target.append(targetNum)
            self.filters.append(filter)


    def process(self,path,config,callback,complete):
        self.logger.info("path="+path)
        self.logger.info("config="+config)

        self.initFilters(config)
        ### read and deal with xls
        (filepath,tempfilename) = os.path.split(path)
        (shortname,ext) = os.path.splitext(tempfilename)
        outputPath = filepath+'/'+shortname+"_result"+ext
        indata = xlrd.open_workbook(path)
        w = xlutils.copy.copy(indata)
        ws = w.get_sheet(0)
        intable = indata.sheets()[0] # TODO to process only the first sheet
        nrows = intable.nrows
        for i in range(nrows ):
            if i==0:
                continue # skip the table head
            results = []
            for filter in self.filters:
                preData = intable.row_values(i)[filter.source]
                result = filter.processor.process(preData)
                if isinstance(result , type([])):
                    if len(result) != (len(filter.target)+1):
                        self.logger.error("result length="+str(len(result)) + "and filter target="+str(filter.target))
                    else:
                        for index in range(len(filter.target)):
                            print result[index]
                            if filter.target[index] == -1 :
                                pass
                            else:
                                ws.write(i,filter.target[index],result[index])
                        results.append(result[-1])

                else: #result not array
                    results.append(result)
            strResult = ""
            for re in results:
                strResult = strResult + str(re) + "|"
            ws.write(i,self.resultColumn,strResult)
            callback(i,nrows)
        print outputPath
        w.save(outputPath)
        complete()
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
        return total-1 # start with 0 not 1

def mainComplete():
    print "Complete"

def mainCallback(index,length):
    print index,length

if __name__ == '__main__':
    logging.config.fileConfig('logging.conf')
    collator = DataCollator()
    # collator.convertLetterToNum('A')
    # collator.convertLetterToNum('B')
    # collator.convertLetterToNum('DF')
    collator.process("../example/1.xlsx","repeat",mainCallback,mainComplete)
    collator.process("../example/2.xlsx","mobileLocate",mainCallback,mainComplete)
