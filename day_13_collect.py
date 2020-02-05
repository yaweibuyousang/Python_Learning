#集合
'''
集合用大括号{}表示，元素间用逗号分隔
建立集合用{}或set{}
建立空集合类型，必须使用set()

集合类型的定义
>>>A = {"python",123,("python",123)}  #使用{}建立集合
{123,'python',('python',123)}
>>>B = set("pypy123")
{'1','p','2','3','y'}
>>>C = {"python",123,"python",123}
{'python',123}

集合操作符
S|T     并
S-T     差
S&T     交
S^T     补
S<=T or S<T 判断ST的子集关系
S>=T or S>T 判断ST的包含关系

S|=T 并，更新集合S，包括在集合S和T中的所有元素
S-=T 差，更新集合S，包括集合S但不在T中的元素
S&=T 交，更新集合S，包括同时在集合S和T中的元素
S^=T 补，更新集合S，包括集合S和T中的非相同元素

eg:
>>> A = {"p","y",123}
>>> B = set("pypy123")
>>> A-B
{123}
>>> A&B
{'p','y'}
>>>A^B
{'2',123,'3','1'}
>>>B-A
{'3','2','1'}
>>>A|B
{'1','p','2','y','3',123}

集合的处理方法
s.add(x) 如果x不在集合S中，将x增加到S
s.discard(x) 移除S中元素x，如果x不在集合S中，不报错
s.remove(x)  移除S中元素x，如果x不在集合S中，产生KeyError异常
s.clear()   移除S中所有元素
s.pop()   随机返回S的一个元素，更新S，若S为空产生KeyError异常

s.copy()  返回集合S的一个副本
len(S)    返回集合S的元素个数
x in S    判断S中元素x，x在集合S中，返回True，否则返回False
x not in S 判断S中元素x，x不在集合S中，返回True，否则返回False
set(x)    将其他类型x转变为集合类型

eg:
>>>A = {"p","y",123}
>>>for item in A:
        print(item,end="")
p123y

>>>A
{'p','123,'y'}


try:
    while True:
        print(A.pop(),end="")
except:
    pass

p123y

>>>A
set()


集合类型应用场景
包含关系比较
eg:
>>> "p" in {"p","y",123}
True
>>>{"p","y"} >= {"p","y",123}
False

数据去重：集合类型所有元素无重复
>>> ls = ["p","p","y","y",123]
>>> s = set(ls)        #利用了集合无重复元素的特点
{'p','y',123}
>>>lt = list(s)        #还可以将集合转换为列表
['p','y',123]


'''
