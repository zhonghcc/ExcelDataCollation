# -*- coding: utf-8 -*-

import baseFilter
import re
import datetime
from filter import dataFilter

@dataFilter("idcard")
class IdCard(baseFilter.BaseFilter):

    def __init__(self):
        pass

    def getReady(self):
        pass

    def process(self,*args):

        if len(args) != 1:
            return "need 1 arg"

        data = args[0]
        data = str(data) #only to judge as text

        if self.isidcard(data)[0] == True:
            return ""
        else:
            return "idcard check error"

    def isidcard(self,id_number):
        area_dict = {11: "北京", 12: "天津", 13: "河北", 14: "山西", 15: "内蒙古", 21: "辽宁", 22: "吉林", 23: "黑龙江", 31: "上海", 32: "江苏",
                     33: "浙江", 34: "安徽", 35: "福建", 36: "江西", 37: "山东", 41: "河南", 42: "湖北", 43: "湖南", 44: "广东", 45: "广西",
                     46: "海南", 50: "重庆", 51: "四川", 52: "贵州", 53: "云南", 54: "西藏", 61: "陕西", 62: "甘肃", 63: "青海", 64: "新疆",
                     71: "台湾", 81: "香港", 82: "澳门", 91: "外国"}
        id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
        if len(id_number) != 18:
            return False, "Length error"
        if not re.match(r"^\d{17}(\d|X|x)$", id_number):
            return False, "Format error"
        if int(id_number[0:2]) not in area_dict:
            return False, "Area code error"
        try:
            datetime.date(int(id_number[6:10]), int(id_number[10:12]), int(id_number[12:14]))
        except ValueError as ve:
            return False, "Datetime error: {0}".format(ve)
        if str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in id_number[0:-1]])]) % 11]) != id_number.upper()[-1]:
            return False, "Check code error"+str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in id_number[0:-1]])]) % 11])
        return True, area_dict[int(id_number[0:2])].decode("utf-8")

if __name__ == '__main__':
    idCard = IdCard()
    print idCard.process("330702196302260412X")
    print idCard.process("3307021963X226041x")
    print idCard.process("330702196呵呵41X")
    print idCard.process("39070219630226041X")
    print idCard.process("33070219630229041X")
    print idCard.process("330702196302260410")
    print idCard.process("33070219630226041x")
    print idCard.process("33070219630226041X")
    print idCard.process("371402198908251914")
    print idCard.process("372901198808065024")
