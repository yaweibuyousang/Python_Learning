#randomNum.py
#random库是使用随机数的Python标准库
#伪随机数：采用梅森旋转算法生成的(伪)随机序列中元素
#random库主要用于生成随机数

'''
基本随机数函数：seed(),random()
扩展随机数函数：randint(),getrandbits(),uniform(),randrange(),choice(),shuffle()

基本随机数函数
seed(a=None)  初始化给定的随机数种子，默认为当前系统时间
>>>random.seed(10) #产生种子10对应的序列

random()    生成一个[0.0,1.0)之间的随机小数
>>>random.random()
0.5714025946899135


扩展随机数函数
randint(a,b)  生成一个[a,b]之间的整数
>>>random.randint(10,100)
64

randrange(m,n[,k])  生成一个[m,n)之间以k为步长的随机整数
>>>random.randrange(10,100,10)
80

getrandbits(k)  生成一个k比特长的随机整数
>>>random.getrandbits(16)
37885

uniform(a,b)  生成一个[a,b]之间的随机小数
>>>random.uniform(10,100)
13.096321648808136

choice(seq)  从序列seq中随机选择一个元素
>>>random.choice([1,2,3,4,5,6,7,8,9])
8

shuffle(seq)  将序列seq中元素随机排列，返回打乱后的序列
>>>s=[1,2,3,4,5,6,7,8,9];random.shuffle(s);print(s)
[3,5,8,9,6,1,2,7,4]
'''

import random
#用法1
random.seed(10)
random.random()

#0.5714025946899135

#用法2
random.random()

#0.4288890546751146

#用法3
random.seed(10)
random.random()

#0.5714025946899135

#用法4
random.seed(10)
random.random()
#0.4714025946899135

#注：使用seed(10)后，生成的第一个随机数必为0.571402546899135

