#8digitalLED.py
'''
函数的定义：
函数是一段代码的表示

def <函数名>(<参数(0个或多个)>):
    <函数体>
    return <返回值>

y = f(x)
(IPO)
函数定义时，所指定的参数是一种占位符
函数定义后，如果不经过调用，是不会被执行
函数定义时，参数是输入，函数体是处理，结果是输出

eg:
def fact(n) :   (函数的定义)
    s = 1        
    for i in range(1, n+1):
        s *= i
    return s

fact(10)  #函数的调用

*注意：
1,调用时，要给出实际参数
2,实际参数替换定义中的参数
3,函数调用后得到返回值
4,函数可以有参数，也可以没有,但必须保留括号
5,函数定义时，可以为某些参数指定默认值,构成可选参数

可选参数传递
eg:(计算n!//m)
def facgt(n,m=1): # m = 1为可选参数，fact(10)默认为m = 1,fact(10,5)m = 5
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m
>>>fact(10)
3628800
>>>fact(10,5)
725760


可变参数传递
函数定义时可以社会可变数量参数，既不确定参数数量
def <函数名>(<参数>,*b)：
    <函数体>
    return <返回值>

eg:(计算n!乘数)
def fact(n,*b): #*b为可变参数
    s = 1
    for i in range(1,n+1):
        s *= i
    for item in b :
        s *= item
    return s

>>>fact(10,3)
10886400
>>>fact(10,3,5,8)
435456000


参数传递的两种方式
函数调用时，参数可以按照位置或者名称方式传递
eg:
def fact(n,m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m

>>>fact(10,5) ==>位置传递
725760
>>>fact(m=5,n=10) ==>名称传递
725760



函数的返回值
函数可以返回0个或多个结果
return 保留字用来传递返回值
函数可以用返回值，也可以没有，可以有return，也可以没有return
return可以传递0个返回值，也可以传递任意多个返回值

eg:
def fact(n,m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s//m, n, m

>>>fact(10,5)
(725760,10,5) ==>元组类型（元组类型类似列表，但不能修改元组中的元素）
>>>a,b,c = fact(10,5)
>>>print(a,b,c)
725760 10 5


局部变量和全局变量
        |        <语句块1>
   程序 |        def <函数名>(<参数>):  |
全局变量|            <函数体>           | 函数
        |            return <返回值>    |局部变量
        |        <语句块2>              |


eg:
n, s = 10,100     <- n,s是全部变量
def fact(n):
    s = 1            fact()函数中的n,s是局部变量
    for i in range(1,n+1):
        s *= i
    return s
print(fact(n),s)

>>>
362800  100


局部变量和全局变量
规则1：局部变量和全局变量是不同变量
局部变量是函数内部的占位符，与全局变量可能重名但不同功能
函数运算结束后，局部变量被释放
可以使用global保留字在函数内部使用全局变量

eg:
n, s = 10, 100
def fact(n):    #fact()函数中s是局部变量与全局变量s不同
    s = 1
    for i in range(1,n+1):
        s *= i
    return s     #此处全局变量s是3628800
print(fact(n),s)  #此处全局变量s是100

>>>
3628800 100


eg:
n, s = 10, 100
def fact(n):    #fact()函数中s使用保留字global声明
    global s = 1  #此处s是全局变量s
    for i in range(1,n+1):
        s *= i
    return s     #此处全局变量s是3628800
print(fact(n),s)  #此处全局变量s被函数修改

>>>
362880000 362880000

局部变量和全局变量
规则2：局部变量为组合数据类型且未创建，等同于全局变量
eg:
ls = ["F","f"]     #通过使用[]真实创建了一个全局变量列表ls
def func(a):
    ls.append(a)    #此处ls是列表类型，未真实创建，则等同于全局变量
    return

func("C")     #此处全局变量ls被修改
print(ls)
['F'.'f','C']

eg:
ls = ["F","f"]      #通过使用[]真实创建了一个全局变量列表ls
def func(a):
    ls = []         #此处ls是列表类型，真实创建，ls是局部变量
    ls.append(a)
    return 

func("C")   #局部变量ls被修改，全局变量ls保持不变
print(ls)

>>>
['F'.'f']


局部变量和全局变量
使用规则：
基本数据类型，无论是否重名，局部变量与全部变量不同
可以通过global保留字在函数内部声明全局变量
组合数据类型，如果局部变量未真实创建，则是全局变量


lambda函数
lambda函数返回函数名作为结果
lambda函数是一种匿名函数，即没有名字的函数
使用lambda保留字定义，函数名是返回结果
lambda函数用于定义简单的，能够在一行内表示的函数

<函数名> = lambda <参数>:<表达式>

                def <函数名>(<参数>):
 等价于：           <函数体>
                    return <返回值>

eg:
>>> f = lambda x, y : x + y
>>> f(10, 15)
25

>>> f lambda : "lambda函数"
>>> print(f())
lambda函数

lambda函数的应用
谨慎使用lambda函数
lambda函数主要用作一些特定函数或方法的参数
lambda函数有一些固定使用方式，建议逐步掌握
一般情况，建议使用def定义的普通函数
'''
