__author__ = 'Liu'
# 导入可以采取import Day40和from Day40 import *。后者无需写类名.函数。前者不容易起冲突
class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_a_song(self):
        for line in self.lyrics:
            print(line)


happy_birthday = song(["Happy birthday to you",
                       "I",
                       "O"])
happy_birthday.sing_a_song()