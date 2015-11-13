# -*- coding: utf-8 -*-
__author__ = 'Liu'

# *args的作用是把所有参数都接收进来，放倒叫args的列表里，一般不怎么用
def print_two(*args):
    arg1, arg2 = args
    print("arg1:%r,arg2:%r" % (arg1, arg2))


# 所以说，这个有没有*args都可以运行，接收参数而已。
def print_two_again(arg1, arg2):
    print("arg1:%r,arg2:%r" % (arg1, arg2))


def print_one(arg1):
    print("arg1:%r" % arg1)


def print_none():
    print("I got nothing")


print_two("刘", "天刘")
print_two_again("Liu", "Liu2")
print_one("Lxxyx")
print_none()

