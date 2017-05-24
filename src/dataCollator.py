# -*- coding: utf-8 -*-

import os
import xlrd
import xlwt
import logging
BASE_PATH = "config/"
class DataCollator():

    def __init__(self):
        self.logger = logging.getLogger("DataCollation.DataCollator")

    def process(self,path,config,callback,complete):
        self.logger.info("path="+path)
        self.logger.info("config="+config)

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
        self.logger.info("你好")
        return configList
