# -*- coding: utf-8 -*-
__author__ = 'Liu'
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', "apriots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# 这里所表示的i，number等都是用来代表每次在这个列表里所取出的元素的
for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("The fruit is %s" % fruit)
for i in change:
    print("I got %r" % i)
elements = []

# range函数会从第一个数到最后一个数但是不包括最后一个数
for i in range(0, 6):
    print("Add %d to the list." % i)
    # 目测append用法同JavaScript.扩充元素
    elements.append(i)

for i in elements:
    print("Elements have %d" % i)