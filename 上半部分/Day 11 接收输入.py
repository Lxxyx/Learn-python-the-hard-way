# -*- coding: utf-8 -*-
__author__ = 'Liu'
print("小姑娘几岁了啊？")
# python 2.x为raw_input函数，而python3.x为input函数
age = input()
print("小姑娘多高了啊？")
height = input()
print("小姑娘多重了啊？")
weight = input()
print("原来是：\n" + age + "岁" + "\n" + height + "公分" + "\n" + weight + "公斤")

# 加上int后，就可以把输入的字符转换为数字，从而进行加减
x = int(input())
y = int(input())

print(x + y)

