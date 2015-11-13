__author__ = 'Liu'
# 其实只是让argv在CMD终端接收一部分的参数，然后在用input函数接收一部分参数
# 并不是用argv的方式，通过输入来接收多个参数
from sys import argv

script, user_name = argv
prompt = ">"
print('My name is %s,and you know i am the script %s.' % (user_name, script))

print('do you like me?')
like = input(prompt)
print("how old are u?")
age = input(prompt)

print("""
Ok you said you %r me very much.you r %r years old.
""" % (like, age)
      )