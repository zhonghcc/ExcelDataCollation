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

        url = "http://cx.shouji.360.cn/phonearea.php?number="+mobile
        req = urllib2.Request(url=url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        print res
        result = json.loads(res)
        provice = result["data"]["province"]
        city = result["data"]["city"]
        sp = result["data"]["sp"]
        self.logger.info(provice+city+sp)
        return [provice,city,sp,""]
    

if __name__ == '__main__':
    mobileLocate = MobileLocate()
    print mobileLocate.process("15806812559")
