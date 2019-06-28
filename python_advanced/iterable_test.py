#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project：project-0610
@Author：shiyao
@Email：13207690135@163.com
@Time：2019-06-18 14:27:20
@IDE：PyCharm
@Project Name：project-0610
@File Name：iterable_test.py
"""


class Test(object):

    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            t = self.i
            self.i = self.i + 1
            return t
        else:
            raise StopIteration('StopIteration...')


o = Test(10)

for i in o:
    print(i)
