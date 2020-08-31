# 如果一个函数在内部调用自身本身，这个函数就是递归函数。
# 计算 n! = 1 x 2 x 3 x ... x n

import sys
sys.setrecursionlimit(1000) # Python 默认递归深度为1000
def fac(n):
    if n == 1:
       return 1
    return n * fac(n -1)

print(fac(100))
 
# print(fac(1000)) # 如果调用深度过大，会存在栈溢出的情况，此时需要通过 【尾递归】进行优化，就是把每一步的乘积传入到递归函数中


def fac_optimize(n):
    return fac_inter(n,1)

def fac_inter(num,product):
    if num == 1:
       return product
    return fac_inter(num -1 ,num * product)

print(fac_optimize(996))