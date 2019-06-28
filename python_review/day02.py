#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Project：project-0610
@Author：shiyao
@Email：13207690135@163.com
@Time：2019-06-18 14:25:15
@IDE：PyCharm
@Project Name：project-0610
@File Name：day02.py
"""

import mysql.connector
from collections import Iterable

config = {'user': 'root', 'password': 'shiyao'}

connection = mysql.connector.connect(**config)

print(connection)

cursor = connection.cursor()

cursor.execute('show databases')

print(isinstance(cursor, Iterable))

for db in cursor:
    print(db)

print('-------------')

cursor.execute('select * from scott.dept')

rows = cursor.fetchall()

for row in rows:
    print(row)
