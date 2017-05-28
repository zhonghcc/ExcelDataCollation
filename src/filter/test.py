# -*- coding: utf-8 -*

def func(a):
    print a

def decorate(name):

    def wrapper(cls):

        print cls
        def wrapper(*args,**kwargs):

            print cls

    return wrapper

@decorate("A")
class A():
    def f1(self):
        print "f1"

