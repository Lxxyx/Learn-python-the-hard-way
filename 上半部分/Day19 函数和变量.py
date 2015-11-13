# -*- coding: utf-8 -*-
__author__ = 'Liu'


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that enough for party")
    print("Get a blanket.\n")

# 可以直接给函数传数字
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# 还能通过input让用户输入数量再输出
cheese_and_crackers(int(input("cheese>")), int(input("crackers>")))

print("Or we can use variable from our script:")
amount_of_cheeses = 10
amount_of_crackers = 50
# 也可以直接给函数传变量
cheese_and_crackers(amount_of_cheeses, amount_of_crackers)

# 还可以给函数传数学表达式
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# 还可以给函数传数学表达式+变量的混合体
print("And we can combine the two,variables and math：")
cheese_and_crackers(amount_of_cheeses + 100, amount_of_crackers + 1000)
