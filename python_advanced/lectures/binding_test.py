#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Time     : 6/17/2019 10:53
# @Author   : mingfei.net@gmail.com
# @FileName : binding_test.py
# @GitHub   : https://github.com/thu/project-0610

class Human(object):
    __slots__ = ('name', 'age')
    pass

tom = Human()
tom.name = 'Tom'

print(tom.name)

tom.age = 18
print(tom.age)

tom.gender = 'Male'
print(tom.gender)


