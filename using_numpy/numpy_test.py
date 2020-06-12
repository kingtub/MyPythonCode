# -*- coding: utf-8 -*-
import numpy
x = numpy.zeros(6, dtype=numpy.int64)  # 创建一维长度为6的，元素都是0一维数组
print(x)
y = numpy.zeros((2, 3))  # 创建一维长度为2，二维长度为3的二维0数组
print(y)

print('x.ndim', x.ndim)
print('y.ndim', y.ndim)
print('x.shape', x.shape)
print('y.shape', y.shape)
print('x.size', x.size)
print('y.size', y.size)
print('x.dtype', x.dtype)
