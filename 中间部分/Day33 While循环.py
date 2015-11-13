# -*- coding: utf-8 -*-
__author__ = 'Liu'
i = 0
number = []

while i < 6:
    print("At the top i is %d" % i)
    number.append(i)
    i += 1
    # 这里的print number是print整个列表，而且列表没有特殊转化，需要用,来添加而不是+号
    print("Number now is", number)
    # 这里的i就只是单纯的I
    print("At the buttom i is %d" % i)

print("The numbers")
for num in number:
    print(num)