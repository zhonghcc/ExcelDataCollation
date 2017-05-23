# -*- coding: utf-8 -*-

import os
import logging
BASE_PATH = "config/"
class DataCollator():

    def __init__(self):
        self.logger = logging.getLogger("DataCollation.DataCollator")

    def process(self,path,config,callback):
        pass

    def getConfigList(self):
        arr = os.listdir(BASE_PATH)
        self.logger.info(arr)
        configList = []
        for fileName in arr:
            fullPath = BASE_PATH + fileName
            print fileName
            if os.path.isfile(fullPath):
                configName,ext = os.path.splitext(fileName)
                configList.append(configName)
        self.logger.info(configList)
        self.logger.info("你好")
        return configList
