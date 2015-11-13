# -*- coding: utf-8 -*-
__author__ = 'Liu'

# 当使用了return之后，则函数会返回一个值。变量或者其他函数可以接收
def add(a, b):
    print("ADDING %d + %d " % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d -%d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDING %d/%d" % (a, b))
    return a / b


print("做些计算吧！")

age = add(30, 5)
height = subtract(200, 30)
weight = multiply(10, 16)
IQ = divide(260, 1)

print("\nAge:%d\nheight:%d\nweigth:%d\nIQ:%d\n" % (age, height, weight, IQ))

# 超级不推荐这种计算，看的头晕
print("超级难的计算")
what = add(age, subtract(height, multiply(weight, divide(IQ, 2))))

print("最后结果是:", what)