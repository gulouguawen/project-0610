#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project：project-0610
@Author：shiyao
@Email：13207690135@163.com
@Time：2019-06-18 14:27:20
@IDE：PyCharm
@Project Name：project-0610
@File Name：generator.py
"""

list_a = list(range(1, 11))

# print(list_a)

# list_a = [x**2 for x in range(1, 11)]

g_a = (x ** 2 for x in range(1, 5))

# print(list_a)
# print(type(g_a))

# print(next(g_a))
# print(next(g_a))
# print(next(g_a))
# print(next(g_a))
# print(next(g_a))

for n in list_a:
    print('n:', n)

for n in g_a:
    print('n:', n)

print('----------')

for n in list_a:
    print('n:', n)

for n in g_a:
    print('n:', n)
