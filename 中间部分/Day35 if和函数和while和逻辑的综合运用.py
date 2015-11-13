# -*- coding: utf-8 -*-
__author__ = "Liu"

from sys import exit
# exit模块的作用在于结束进程

def gold_room():
    print("This room is full of gold.How  much do you take?")

    next = input(">")
    # 这一段的意思非常巧妙，指的是如果你输入的数字没有1或者0，直接退出游戏。
    # 如果有1或0，则把输入的金额转换为数字，再通过下面的判断。
    # 以后的if判断可以通过判断某个字符是否在某个字符串内来判定
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man,learn to type a number.")
    if how_much < 50:
        print("You are not greedy.You win!")
        exit(0)
    else:
        # 这儿的dead()是个函数，用来接收死亡信息并且结束进程
        dead("You greedy bastard.")


def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # bear_moved表示熊是否移动
    bear_moved = False

    # 利用while循环和bear_moved进行判断，如果要进房子只有bear_moved==true才行。
    # While True可以创建无限循环。这时候只能内部跳出。
    while True:
        next = input("Take honey?\tTanut bear?\topen door?\n>")
        if next == "Take honey":
            dead("The bear eats you.")
        elif next == "Taunt bear" and not bear_moved:
            print("The bear moved,You can go.")
            bear_moved = True
        elif next == "Taunt bear" and bear_moved:
            dead("Bear eats you")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I don't know what's your meaning")


def cthulhu_room():
    print("Here you see the great evil cthulhu.")
    print("Do you flee or eat your head?")
    next = input("flee or head?\n>")
    # 每一个if语句都要有else，就算没有什么意义
    # if嵌套最好不要超过两层，如果if里面又有if，最好把它移到另外一个函数里
    if "flee" in next:
        start()
    elif "head" in next:
        dead("You have been eat!")
    else:
        cthulhu_room()


def dead(why):
    print(why + "Good job!")
    exit(0)


def start():
    print("You are in a dark room")
    print("There is a door to your right and left")
    print("Which one do you take?")
    next = input("left or right?\n>")
    if "left" in next:
        bear_room()
    elif "right" in next:
        cthulhu_room()
    else:
        dead("You are starved to death")


start()