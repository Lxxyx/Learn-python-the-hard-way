# -*- coding: utf-8 -*-
__author__ = 'Liu'
from 笨方法学Python.上半部分 import Day25

sentence = "All good things come to those who wait."
words = Day25.break_words(sentence)
print(words)
sorted_words = Day25.sort_words(words)
print(sorted_words)
print(Day25.print_first_word(words))
print(Day25.print_last_word(words))
