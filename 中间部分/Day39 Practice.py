# -*- coding: utf-8 -*-
__author__ = 'Liu'
states = {
    'Oregon': 'Or',
    'Florida': 'fl',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'Mi'
}

cities = {
    'CA': 'Sanfransico',
    'MI': 'Detroit',
    'FL': 'Jack'
}
cities['NY'] = 'New york'
cities['OR'] = 'Fortland'
print("-" * 10)
print("NY state has:", cities['NY'])
print("OR state has:", cities['OR'])

for state, abbrev in states.items():
    print("%s stater is %s " % (state, abbrev))

