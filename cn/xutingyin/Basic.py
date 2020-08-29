# --------------------------Python 基本语法---------------------------
# 1、Python 使用 # 进行注释
# 2、Python 严格区分大小写
#---------------数据类型------------------
# 整数 -- Python 中变量前不用定义数据类型，解释器会根据你的赋值直接判断是什么数据类型。这一点和Java|C语言不一样。Python是解释性语言[动态语言]、而Java是静态语言
a = 200
print(a)
# 浮点数
b = 0.85
c = 2.3e8  # 可以使用科学计数法表示浮点数
print(b)
print(c)
# 字符串
str = "Hello,Python."
print(str)

# 如果字符串中包含特殊字符，需要使用转义符号
str2 = "I\'m learning \n Python."
print(str2)
# 布尔值 只有 True|False 两种取值，注意区分大小写；布尔值可以使用 and,or和not 进行逻辑运算

print(True and True)
print(3>2 and 1>2) # Flase,and 运算是与运算，只有运算符两边的表达式都为True最终的结果才为True
print(not 3>2) # False,not 为非运算，取反操作

# 空值，Python 中None 代表一个特殊的值，空值

# 变量，Python中定义一个变量，只需要一个变量名即可，不用申明数据类型。变量名的命名规则：必须是大小写英文、数字和_的组合，且不能用数字开头
# 变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错
int_a=100
print("int_a=",int_a)
str = "Hello,Python!"
print("str=",str)
boolFlag = True
print("boolFlag=",boolFlag)

# 常量，原则上规定全是大写字母表示，例如 PI;实则还是一个变量，因为Python没有机制保证它的值不会被改变

#-------------------------------------------华丽分割线---------------------------------------
# 字符编码 ：ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节
# 把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间
# 计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('哈'))
print(chr(66))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len("中文"))
print(len("ABC"))
print(len("中文".encode("UTF-8"))) # 6， 一个中文通常使用三个字节
print(len("ABC".encode("utf-8")))

# 格式化: %d-整数;%s-字符;%f-浮点数,如果指定了保留了几位小数，则会四舍五入;%x-十六进制整数
print("尊敬的客户， %s,您本月消费：￥%.2f" %("马云",9699.692))


# list，有序列表，下标从0开始
classmates =["susan","Lily","Herby"]
print(classmates)
print(classmates[2])
classmates.append("Nike") # 尾部追加元素
print(classmates)
classmates.pop(1) # 根据数组下标删除元素
print(classmates)

# tuple tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
# 但是classmates2这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
classmates2 = ('Michael', 'Bob', 'Tracy')
print(classmates2)

# 条件判断 - 只要满足一个条件，后面的if 就会别忽略掉了
age = 20
if (age >= 6 and age < 20):
    print("teenager")
elif age>=20:
    print("adult")
else:
    print("kid")

# sbirth = input('birth: ')
sbirth = '20'
birth =int(sbirth)
if birth < 2000 : 
  print("00前")
else:
  print("00后")

## Demo 练习，计算BMI(体重除以身高的平方),判断体重标准。体重 71KG，身高 168cm
bmi = round(71/(1.68*1.68),2)
print("bmi=",bmi)
if bmi< 18.5:
   print("过轻")
elif 18.5<=bmi and bmi<25:
   print("正常")
elif 25<=bmi and bmi<28:
   print("过重")
elif 28<=bmi and bmi<32:
   print("肥胖")
else:
  print("严重肥胖")


# 循环
# ---for in 循环
# 计算 1-100 之和 ,range(n)函数用于产生0-(n-1)之间的整数
lists=list(range(101))
sum = 0
for index in lists :
  sum = sum + index
print("sum=",sum)

# while 循环
# 计算 0-99 之间的奇数之和
sum = 0
n = 99
while n > 0 :
    sum = sum + n
    n = n -2
print("sum=",sum)

# 跳出循环 
# break
print("--------------大于10 break---------------------")
n = 1
while n < 100 :
  if n > 10 :
   break
  print("n=",n)
  n = n + 1
print("--------------continue---------------------")
n = 0
while n < 10 :
    n = n + 1
    if n % 2 == 0 :
      continue
    print(n)
 
# dict 全称dictionary，相当于Java 中Map
print("-----------------dict-----------------------")
scores = {"Susan":90,"Lily":92,"Herby":99,"John":89}
#  获取key对应的值，有两种方式
# 方式1 通过[key] 获取
print("Susan's grade:",scores["Susan"])
# 方式2 get(key) 获取
print("Susan's grade:",scores.get("Susan"))
print("Susan's grade:",scores.get("Susan1"))
print("Susan's grade:",scores.get("Susan2",0)) # 如果dict 中不存在，会返回空值None,此时我们可以自定义一个返回值

# 删除元素
scores.pop("Susan")
print(scores)
# 添加元素 -尾部添加
scores["一沐"]=96
print(scores)

'''
多行注释 使用 三个单引号或者双引号
看到这里，我们可以发现dict 和list 有点类似，但是他们存在一些区别：
   
    和list比较，dict有以下几个特点：

    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
    而list相反：

    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法。 

'''
# set ---只存放key,不存放value;并且key不能重复，如果重复会被覆盖
print('----------------------set--------------------')
s = set([1,2,3,4,5])
print(s)

# 添加key-尾部添加
s.add(6)
print(s)
# 删除 key
s.remove(1)
print(s)

# set 可以看做是无序、无重复元素的集合，那么就可以使用set 做数学意义上的交集、差集、并集等运算
print('---------------------set 集合运算-------------')
s1 = set([1,2,3,4])
s2 = set([3,4,5,6])
print("[交集]：s1 & s2 = ",s1 & s2)
print("[并集集]：s1 | s2 = ",s1 | s2)
# 差集 两种方式
print("[差集]：s1 - s2 = ",s1 - s2)
print("[差集]：s1.difference(s2) = ",s1.difference(s2))

# 对称差集 ：相当于两个集合的补集的并集 AΔB = (A—B)∪(B—A)
print('[对称差集]：s1.symmetric_difference(s2)=',s1.symmetric_difference(s2))

# 不可变对象
print('----------------------不可变对象-----------------------')
# 先看可变对象，比如list，对list进行操作，list内部的内容是会变化的，例如
a = ['a','c','d','b']
a.sort()
print(a) # 会改变原来的顺序，结果为a,b,c,d

# 不可变对象
str1 = 'abc'
str2 = str1.replace('a','A')
print("str1=",str1) #str1 指向的内容还是 abc，没有改变
print("str2=",str2)

'''
    当我们调用str1.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，
    但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，
    如果我们用变量b指向该新字符串，就容易理解了，变量str1仍指向原有的字符串'abc'，但变量str2却指向新字符串'Abc'了：
'''



































