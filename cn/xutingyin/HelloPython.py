# Python 简介
# 著名的“龟叔”Guido van Rossum在1989年圣诞节期间，为了打发无聊的圣诞节而编写的一个编程语言。
# 龟叔给Python 的定义就是“优雅”、“明确”、“简单”。
# Python 的缺点：①运行速度慢 ；②代码不能加密
# Python 的解释器有很多，默认使用CPython,官方安装包默认已集成。其它的解释器还有例如：IPython,PyPy,Jython等等
# Python 有两种模式，一种是Python 交互模式，在命令行输入python ，便可以看到使用>>> 提示的Python交互模式；另外一种就是命令行模式，直接编写一个.py结尾的文件，使用 python xxx.py 运行
print("Hello,Python!")
# 自定义变量名，无需指定数据类型
name = 100 + 200
print(name)
# 输出多个数据，并且还是不同的数据类型
print("123", "hello", "jjjj", 123 * 123)
length = len("哈哈".encode("utf-8"))
print(length)
print(2**10)
name = input("Please input your name:\n")
print("hello",name)