#程序分支结构
'''
单分支结构
二分支结构
多分支结构
条件判断及组合
程序的异常处理


1)单分支结构：
if <条件>:
    <语句块>

eg:
    guess = eval(input())                               
    if guess == 99:                    if True:
    print("猜对了")                        print("条件正确")


2)二分支结构：
(根据判断条件结果而选择不同向前路径的运行方式)
if <条件>:
    <语句块1>

else:
    <语句块2>

eg:
    guess = eval(input())             if True:         
    if guess == 99:                       print("语句块1")
        print("猜对了")               else:
    else:                                 print("语句块2")
        print("猜错了")

二分支紧凑形式：适用于简单表达式的二分支结构
<表达式1> if  <条件> else <表达式2>
eg:
guess eval(input())
print("猜{}了".format("对" if guess==99 else "错"))

3)多分支结构
if <条件1> ：
    <语句块1>
elif <条件2>：
    <语句块2>
    ...
else:
    <语句块N>

score = eval(input())
if score >=60:
    grade = 'D'
elif score >=70:
    grade = 'C'
elif score >=80:
    grade = 'B'
elif score >=90:
    grade = 'A'
print("输入成绩属于级别{}".format(grade))


程序的控制结构
1，顺序结构
2，分支结构
3，循环结构

条件组合：
x and y  ==  x & y
x or y  ==  x | y
not x  ==  !x

条件判断及组合：
eg:
guess = eval(input())                   if not True:
if guess > 99 or guess < 99:                print("语句块2") 
    print("猜错了")                     else:
else:                                       print("语句块1")   
    print("猜对了")

异常处理
try :                               try:
    <语句块1>                           <语句块1>
except:                             except <异常类型> : 
    <语句块2>                            <语句块2>

eg:
try :
    num = eval(input("请输入一个整数："))
    print(num**2)

except:
    print("输入不是整数")


try :
    num = eval(input("请输入一个整数："))
    print(num**2)
except NameError:  #注：标注异常类型后，仅响应此类异常，异常类型名字等同于变量名
    print("输入不是整数")


异常处理的高级使用：
try :
    <语句块1>
except :
    <语句块2>
else :     #注：else对应语句块3在不发生异常时执行
    <语句块3>
finally :  #注：finally对应语句块4一定执行
    <语句块4>

'''
