# -*- coding: utf-8 -*-
__author__ = 'Liu'


# script, in_file, out_file = argv
# 通过输入等方式传入文件名字
in_file = input("input>")
out_file = input("output>")


def copy(*args):
    # 把传入的名字分配给input和output
    input, output = args
    in_file = open(input)
    indata = in_file.read()
    out_file = open(output, 'w')
    out_file.write(indata)


copy(in_file, out_file)