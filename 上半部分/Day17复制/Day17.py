# -*- coding: utf-8 -*-
__author__ = 'Liu'
from sys import argv
# 插入的exists模块的作用的是检测该文件是否存在
from os.path import exists

script, from_file, to_file = argv

print("Copying for %s to %s" % (from_file, to_file))
# 此处in_file作为的是打开的文件，indata是文件的内容
in_file = open(from_file).read()
indata = in_file.read()

print("This input file is %d bytes long" % len(indata))

print("Does the output file exist?---->%r" % exists(to_file))
print("Ready,hit return to continue,ctrl+c to abort")
input()

out_file = open(to_file, 'w')
# 相当于把indata的内容写入out_file
out_file.write(indata)

print("All right,Well done")
out_file.close()
in_file.close()

