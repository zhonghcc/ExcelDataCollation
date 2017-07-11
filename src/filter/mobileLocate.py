# -*- coding: utf-8 -*-

import baseFilter
import re
import datetime
import urllib2
import json
from filter import dataFilter
import logging


@dataFilter("mobileLocate")
class MobileLocate(baseFilter.BaseFilter):

    def __init__(self):
        self.logger = logging.getLogger("DataCollation.filter.mobileLocate")
        pass

    def getReady(self):
        pass

    def process(self,*args):

        if len(args) != 1:
            return "need 1 arg"

        data = args[0]
        data = str(data) #only to judge as text

        return self.locate(data)

    def locate(self,mobile):

        url = "http://cx.shouji.360.cn/phonearea.php?number="+str(mobile)
        #print url
        self.logger.info(url)
        req = urllib2.Request(url=url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        self.logger.info(res)
        result = json.loads(res)
        print result
        provice = ""
        city = ""
        sp = ""
        err = ""
        if result["code"]==0:
            provice = result["data"]["province"]
            city = result["data"]["city"]
            sp = result["data"]["sp"]
            self.logger.info(provice+city+sp)
        else:
            err = str(mobile)+"error"
        self.logger.info([provice,city,sp,err])
        return [provice,city,sp,err]
    

if __name__ == '__main__':
    mobileLocate = MobileLocate()
    print mobileLocate.process("15806812559")
