# 自定义函数： 使用 def 关键字定义
print("--------自定义绝对值函数-------------")
def my_abs(x):
    if not isinstance(x, (int, float)):  #isinstance() 来处理数据类型检查
        raise TypeError('bad operand type')
    if(x >= 0):
       return x
    else:
       return -x

print(my_abs(-10))

# 空函数 
def nop():
    pass  #pass语句什么都不做，这里用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

# 函数返回多个值
print('------------函数返回多个值--------------')
import math # 导入 math 包，这样便可以使用里面的所有函数，例如sin、cos等
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx , ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

# 位置参数
print("---------------计算x的n次方--------")
# n =2 为经常计算x的平方，我们可以使用默认参数，这样就可以省略传入的位置参数；如果想计算其它次方，则需要明确指定n 的值
def power(x,n=2):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

print(power(4))