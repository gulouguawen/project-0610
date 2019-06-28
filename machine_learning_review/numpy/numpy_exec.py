#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @Project：project-0610
# @Author：shiyao
# @Email：13207690135@163.com
# @Time：2019-06-21 15:56:19
# @IDE：PyCharm
# @Project Name：project-0610
# @File Name：numpy_exec.py

from numpy import *  # 不推荐直接引用模块内全部内容
import matplotlib.pyplot as plt
from numpy.random import rand

# 1. 安装 Numpy
# conda install numpy

# 2. a = [1, 2, 3, 4]，使用 Numpy 将每个元素 + 1
a = [1, 2, 3, 4]
a = array(a)
print(a + 1)

# 3. b = [4, 5, 6, 7]，使用 Numpy 将 a 和 b 对应元素相加
b = [4, 5, 6, 7]
print(a + b)

# 4. 将 a 转换为 2×2 的二维数组
a.shape = 2, 2
print(a)

# 5. 根据以下代码绘制曲线图
a = linspace(0, 2 * pi, 21)
print(a)
b = sin(a)

# conda install matplotlib
plt.plot(a, b)
# plt.show()

# 6. 选取 b 中所有的非负值

print(b >= 0)

# 7. 绘制 a, b 对应的非负值的点
mask = (b >= 0)
plt.plot(a[mask], b[mask], 'ro')
# plt.show()

# 8. 求 a 所有元素的和
print(a)
print(sum(a))
# 9. 求 a 所有元素乘积
print(prod(a))
# 10. 求以下 a 的全局最大最小值
a = rand(3, 4)
print(a)
print('min:', a.min())
print('max:', a.max())

# 11.求 a 的均值
a = array([[1, 2, 3], [4, 5, 6]])
print(a.mean())

# 12. 求 a 的标准差
print(a.std(axis=1))

# 13. 求 a 的方差
print(a.var(axis=1))

# 14. 把 a 限制在 [3,5] 范围内
a = array([[1, 2, 3],
           [4, 5, 6]])
print(a.clip(3, 5))

# 15. 把 a 近似到整数和一位小数
a = array([1.35, 2.5, 1.5])
print(a.round())  # .5 的近似，取向最近的偶数

# 16. 把数组修改为 2×3
a = arange(8)
print(a)
a.shape = 2, 4
print(a)

# 17. 对 a 做转置

a = array([[[0, 1, 2]],

           [[3, 4, 5]]])

print(a.transpose())
print(a.T)

# 18. 将 a 转为一维数组

a = array([[0, 1],
           [2, 3]])

print(a.flatten())

# 19. 求 a 的对角线

a = array([11, 21, 31, 12, 22, 32, 13, 23, 33])
a.shape = 3, 3
print(a)
print(a.diagonal())

# 20. 求 a 的右移 1 次对角线
print(a.diagonal(offset=1))
print(a.diagonal(offset=2))
print(a.diagonal(offset=-2))

# 21. 求 a 的基本属性：数据类型/形状/元素数目/一个元素&所有元素占用字节/维度
a = array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print(a.dtype)
print(a.shape)
print(a.size)
print(a.itemsize)
print(a.nbytes)
print(a.ndim)  # dim =dimension

# 22. a 转为list
print(a.tolist())

# 23. a 转为 float
print(a.astype(float))

# 24. a 存为文件
save("array", a)

# 25. 从文件中取出 a
print("load:", load("array.npy"))

# 26. 使用 `arange` 生成 [0, 10] 一维数组
a = arange(11)
print(a)

# 27. 使用 `linspace` 生成 [0, 1] 五等分一维数组
a = linspace(0, 1, 5)
print(a)

# 28. 使用 `r_` 生成 [0, 1] 十等分行向量
a = r_[0:1:.1]
print(a)

# 29. 使用 `c_` 生成 [1, 5] 十等分列向量
a = c_[1:5:.4]
print(a)

# 30. 把 a 转为矩阵
a = array([[1, 2, 4],
           [2, 5, 3],
           [7, 8, 9]])

print('array:', a, 'type:', type(a))

a = mat(a)

print('matrix:', a, 'type:', type(a))
