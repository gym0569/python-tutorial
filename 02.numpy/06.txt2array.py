# -*- coding: utf-8 -*-
"""
@description:
@author:XuMing
"""
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np

# 从文本中读取数组

# 对于文本文件，推荐使用
# loadtxt
# genfromtxt
# savetxt

# 对于二进制文本文件，推荐使用
# save
# load
# savez
c = np.loadtxt("data.txt", dtype=int)
print(c)
# 解释一下：
# loadtxt 函数
# loadtxt(fname, dtype=<type 'float'>,
#         comments='#', delimiter=None,
#         converters=None, skiprows=0,
#         usecols=None, unpack=False, ndmin=0)
#
# loadtxt 有很多可选参数，其中 delimiter 就是刚才用到的分隔符参数。
# skiprows 参数表示忽略开头的行数，可以用来读写含有标题的文本

# 此外，有一个功能更为全面的 genfromtxt 函数，
# 能处理更多的情况，但相应的速度和效率会慢一些。
g = np.genfromtxt("data.txt")
print(g)

# 当然，还有很笨的写法：
# 首先将数据转化成一个列表组成的列表，再将这个列表转换为数组：
data = []

with open('data.txt') as f:
    # 每次读一行
    for line in f:
        fileds = line.split()
        row_data = [float(x) for x in fileds]
        data.append(row_data)

data = np.array(data)
print(data)

# loadtxt 的更多特性
data = np.loadtxt('special_data.txt',
                  dtype=np.int,
                  comments='%',  # 百分号为注释符
                  delimiter=',',  # 逗号分割
                  skiprows=1,  # 忽略第一行
                  usecols=(0, 1, 2, 4))  # 指定使用哪几列数据
print(data)

# loadtxt 自定义转换方法
import datetime


def date_converter(s):
    return datetime.datetime.strptime(s, "%Y-%m-%d")


data = np.loadtxt('datetime_data.txt',
                  dtype=np.object,  # 数据类型为对象
                  converters={0: date_converter,  # 第一列使用自定义转换方法
                              1: float,  # 第二第三使用浮点数转换
                              2: float})

print(data)

# pandas ——一个用来处理时间序列的包中包含处理各种文件的方法，
# 具体可参见它的文档：
# http://pandas.pydata.org/pandas-docs/stable/io.html
