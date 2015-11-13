# -*- coding: utf-8 -*-
__author__ = 'Liu'
# 通过argv来获取文件名字，script属于必要参数。不然无法接收filename
from sys import argv

script, filename = argv

# 通过建立变量txt来打开刚才所接收的文件
txt = open(filename)
print("here is you file %r:" % filename)
print(txt.read())

# 再次输入名字而已，操作步骤和逻辑同上
print("Type the file name again:")
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())