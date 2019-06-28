#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time     : 6/17/2019 10:29
# @Author   : mingfei.net@gmail.com
# @FileName : oop_test.py
# @GitHub   : https://github.com/thu/project-0610


class Human(object):

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

tom = Human('Tom', 18)

# print(tom.name)

# tom.__age = 19
#
# print(tom.__age)

# print(tom.get_age())


def fn_study(x):
    x.study()


# fn_study(tom)

class Duck(object):

    def study(self):
        pass


d = Duck()

fn_study(d)


print(type(abs))

import types

print(type(fn_study) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)  # ***

print(dir(tom))

print(tom.__class__)

print(tom.__dir__())

print(getattr(tom, 'get_age'))

from types import MethodType


def get_name(self):
    return self.name

Human.get_name = get_name
# tom.get_name = MethodType(get_name, tom)  # binding method

print(tom.get_name())

jerry = Human('Jerry', 19)

print(jerry.get_name())



