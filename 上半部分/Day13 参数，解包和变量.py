# -*- coding: utf-8 -*-
__author__ = 'Liu'
from sys import argv

# 解包就是输入时把所有参数赋予argv，然后argv再把所有参与一个一个的赋予给前面的参数
# 此过程需要在CMD终端下完成
script, first, second, third = argv

# 该方法需要把参数放在括号里面,script接收的是当前Python脚本的信息
print("The Script is called", script)
print("1", first)
print("2", second)
print("3", third)