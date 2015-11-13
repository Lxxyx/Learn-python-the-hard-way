# -*- coding: utf-8 -*-
__author__ = 'Liu'

ten_things = "Apple Oranges Crows Telephone Light Suagr"
print("Wait there's not 10 things in that list,let's fix that.")
stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # 把more_stuff的最后一位弹出
    # 再用stuff的append接收
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There is %d items now." % len(stuff))

print("There we go:", stuff)

print("Let's do some things with stuff.")

# 是orange的原因在于它是1位置，列表从0开始
print(stuff[1])
print(stuff[-1])
# -1是显示最后一个，pop是弹出最后一个。
print(stuff.pop())

print(" ".join(stuff))
print("#".join(stuff[3:5]))