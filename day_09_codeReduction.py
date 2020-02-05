#codeReduction.py
'''
代码复用
函数和对象是代码复用的两种主要形式
函数：将代码命名在代码层面建立了初步抽象

对象：属性和方法
<a>.<b>和<a>.<b>()
在函数之上再次组织进行抽象

模块化设计
分而治之
通过函数或对象封装将程序划分为模块及模块间的表达
具体包括:主程序，子程序和子程序间关系
分而治之:一种分而治之，分层抽象，体系化的设计思想


紧耦合 松耦合
紧耦合:两个部分之间交流很多，无法独立存在
松耦合:两个部分之间交流较少，可以独立存在
模块内部紧耦合，模块之间松耦合


递归的定义
函数定义中调用函数自身的方式
链条：计算过程存在递归链条
基例：存在一个或多个不需要再次递归的基例
数学归纳法
证明当N取第一个值N0时成立
假设Nk成立，证明Nk+1成立



递归的实现：
        1       n=1
 n!=   
        n(n-1)! otherwise

def fact(n):
    if n == 0 :
        return 1
    else :
        return n*fact(n-1)

递归的实现：
函数 + 分支语句
递归本身是一个函数，需要函数定义方式描述
函数内部，采用分支语句对输入参数进行判断
基例和链条，分别编写对应代码

eg:#字符串反转输出
>>>s[::-1]

def rvs(s):
    if s == "":
        return s
    else :
        return rvs(s[1:])+s[0]

#斐波那契数列
F(n)=F(n-1)+F(n-2)
def f(n):
    if n == 1 or n == 2:
        return 1
    else :
        return f(n-1) + f(n-2)

#汉诺塔
count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count += 1
        hanoi(n-1,mid,dst,src)

hanoi(10,"A","B","C")
print(count)
'''
