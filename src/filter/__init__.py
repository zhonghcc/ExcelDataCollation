# -*- coding: utf-8 -*

filtersClass={}

def dataFilter(name):

    def decorator(cls):

        filtersClass[name]=cls
        print "register "+name

    return decorator
