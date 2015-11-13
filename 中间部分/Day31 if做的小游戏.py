# -*- coding: utf-8 -*-
__author__ = 'Liu'
print("你进了一个小黑屋，前面有两扇门，你要选1号还是2号？")
door = input("输入1或者2:\n>")
if door == "1":
    print("一号门里有大熊正在吃蛋糕，这时候你会做什么？\n1.拿走熊的蛋糕\n2.对熊怒吼")
    bear = input("请输入1或者2:\n>")
    if bear == "1":
        print("熊吃了你")
    elif bear == "2":
        print("熊被你吓跑了")
    else:
        print("输入错误，请重新输入")
elif door == "2":
    print("后面的英语太复杂，少侠请回吧！")
else:
    print("Hello World!")