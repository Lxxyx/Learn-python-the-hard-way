# -*- coding: utf-8 -*-
__author__ = 'Liu'
people = 20
cats = 30
dogs = 15

if people < cats:
    print("There are too many cats")
else:
    print('Too Many people')
if people > dogs:
    print("Dogs are less than people")
else:
    print("People are less than dogs")

dogs += 5

# 如果用的是elif，则只要一个if成立，下面的所有elif都不执行
if people >= dogs:
    print("People>=dogs")
if people <= dogs:
    print("People<=dogs")
if people == dogs:
    print('They are same')