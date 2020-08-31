#!/usr/bin/python
# -*- coding: utf-8 -*-
# --------------函数-------------
# python 内置了许多函数，我们直接调用
# 绝对值
a = abs(-10)
print(a)

# 最大值
b = max(-1,2,4)
print(b)
# 最小值
c = min(1,22,90)
print(c)

# 数据类型转换
print('-----------数据类型转换--------------')
int_a = int('123')
print(int_a)

float_b = float('22.89')
print(float_b)
print('------------bool 操作-------------')
bool_c = bool(1)
bool_d = bool('') # False
bool_e = bool("") # False
bool_f = bool(()) # False
bool_g = bool([]) # False
bool_h = bool({}) # False
'''
    Python 中，一下情况，bool 操作会被认为是False
    为0的数字，包括0，0.0
    空字符串，包括'', ""
    表示空值的None
    空集合，包括()，[]，{}
    其他的值都认为是True。
'''
print(bool_c)
print(bool_d)
print(bool_e)
print(bool_f)
print(bool_g)
print(bool_h)
