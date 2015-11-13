# -*- coding: utf-8 -*-
__author__ = 'Liu'
from sys import argv

script, filename = argv
# 先输出文本中已经有的内容，用的是open和read两个函数
targettest = open(filename)
print(targettest.read())

print("We are going to erase %r." % filename)
print("If you don't that ,hit ctrl+c (^c).")
print("If you want that , hit return.")
# 只是个噱头，然并卵，不过挺好看
input("?")

print("Opening the file...")
# w参数是指以写方式打开
target = open(filename, 'w')

print("Truncating the file.Good bye")
# 会清空文件内容
target.truncate()

print("Now i'm going to ask you for three lines.")
# 输入三行要写的东西
line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("I'm going to write these to the file.")
# 写入文件，一行一行的写入
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we will close it")
# 关闭文件，释放资源
target.close()