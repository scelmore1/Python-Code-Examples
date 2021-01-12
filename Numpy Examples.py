# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0901

Scott Elmore
11/15/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/jwZS-BbqeM8
"""

# numpy package
import numpy as np

# array 0-99
a = np.arange(0, 100)
print('2:\n', a)

# array 0-99 by 10
b = np.arange(0, 100, 10)
print('3:\n', b)

# array 0-10 by .1
c = np.linspace(0., 10., num=101)
print('4:\n', c)

# random 2d array 10x10
d = np.random.random((10, 10))
print('5:\n', d)

# a is now 10x10
a = a.reshape(10, 10)
print('6:\n', a)

# access array element at row 4 column 5 (0 index)
print('7:\n', a[4, 5])

# access array row at row 4
print('8:\n', a[4])

# sum the entire array
print('9:\n', d.sum())

# get max of entire array
print('10:\n', a.max())

# transpose array b
print('11:\n', b.transpose())

# matrix addition
print('12:\n', a + d)

# matrix multiplication (element by element)
print('13:\n', a * d)

# dot product
print('14:\n', np.dot(a, d))
