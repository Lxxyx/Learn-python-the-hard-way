# -*- coding: utf-8 -*-
__author__ = 'Liu'

stuff = {'name': 'liu', 'age': '36', 'height': '6*12+2'}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

print(stuff)
# 这里的city加入要用下面的方式，而不是和stuff创建。
stuff['city'] = 'shanghai'

print(stuff)
stuff[1] = "wow"
print(stuff)

del stuff['city']
del stuff[1]

print(stuff)