#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project：project-0610
@Author：shiyao
@Email：13207690135@163.com
@Time：2019-06-18 14:27:20
@IDE：PyCharm
@Project Name：project-0610
@File Name：decorator_test.py
"""


def a_decorator(func):
    def wrapper(*args, **kwargs):  # arguments
        print(func.__name__, 'before...')
        func(*args, **kwargs)
        print(func.__name__, 'after...')

    return wrapper


@a_decorator
def f():
    print('function f...')


@a_decorator
def foo(name):
    print('hi', name)


# f()

# f = a_decorator(f)

# f()

foo('Tom')
