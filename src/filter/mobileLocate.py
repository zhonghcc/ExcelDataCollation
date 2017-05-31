# -*- coding: utf-8 -*-

import baseFilter
import re
import datetime
import urllib2
import json
from filter import dataFilter


@dataFilter("mobileLocate")
class MobileLocate(baseFilter.BaseFilter):

    def __init__(self):
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

        url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel="+mobile
        req = urllib2.Request(url=url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        res = unicode(res,"gbk").replace("__GetZoneResult_ =","")
        arr = res.split("'")
        #result = json.loads(res)
        return [arr[3],arr[5],""]
    

if __name__ == '__main__':
    mobileLocate = MobileLocate()
    print mobileLocate.process("15806812559")
