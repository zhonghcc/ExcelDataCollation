# -*- coding: utf-8 -*-

import baseFilter
from filter import dataFilter

@dataFilter("repeat")
class Repeat(baseFilter.BaseFilter):

    def __init__(self):
        self.set = set()
        pass

    def getReady(self):
        self.set.clear()

    def process(self,*args):

        if len(args) != 1:
            return "need 1 arg"

        data = args[0]
        data = str(data) #only to judge as text
        if data in self.set:
            return data+"repeat"
        else:
            self.set.add(data)
            return ""



if __name__ == '__main__':
    repeat = Repeat()
    repeat.getReady()
    print(repeat.process("13800138000"))
    print(repeat.process("13800138000"))
    print(repeat.process("13800138001"))
