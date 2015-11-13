# -*- coding: utf-8 -*-
__author__ = 'Liu'
from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


# seek的用法有待商榷,目前看来是定位到文件开头
def rewind(f):
    f.seek(0)


# readline用法比较神奇,它会在读到\n换行符时候停止，还会记录位置，避免重复读取
def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)
print("Fist let's print the whole file:\n")
print_all(current_file)

print("Now Rewind")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
