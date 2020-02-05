#循环
'''
1)遍历循环
遍历某个结构形成的循环运行方式
for <循环变量> in <遍历结构>:
    <语句块>

    从遍历结构中逐一提取元素，放在循环变量中
    完整遍历所有元素后结束
    每次循环，所获得元素放入循环变量，并执行一次语句块

应用：
①计数循环(N次)
for i in range(N):
    <语句块>

    遍历由range()函数产生的数字序列，产生循环
eg:
    for i in range(5):
        print(i)
②计数循环(特定次)
for i in range(M,N,K):
    <语句块>
eg:
    for i in range(1,6,2)
③字符串遍历循环
for c in s :
    <语句块>
s是字符串，遍历字符串每个字符，产生循环
eg:
for c in "Python123":
    print(c,end=",")

p,y,t,h,o,n,1,2,3,
④列表遍历循环
for item in ls :
    <语句块>
    ls是一个列表，遍历其每个元素，产生循环
eg:
for item in [123,"PY",456]
    print(item,end=",")

123,PY,456,
⑤文件遍历循环
for line in fi :
    <语句块>
fi是一个文件标识符，遍历其每行，产生循环


2)无线循环
由条件控制的循环运行方式
while <条件> :
    <语句块>
反复执行语句块，直到条件不满足时结束
eg:
a = 3
while a > 0 :
    a = a - 1
    print(a)

(CTRL + C退出执行)

3)循环控制保留字
break 和 continue
-break跳出并结束当前整个循环，执行循环后的语句
-continue结束当次循环，继续执行后续次数循环
-break和continue可以与for和while循环搭配使用

eg:
for c in "PYTHON" :                           for c in "PYTHON" :
    if c == "T":                                   if c == "T" : 
        continue                                      break
    print(c,end="")                                print(c,end="")


PYHON                                         PY


eg:
s = "PYTHON"                                  s = "PYTHON" :
while s != "" :                               while s != "" :    
    for c in s :                                   for c in s :
        print(c,end="")                                if c == "T" :
    s=s[:-1]                                              break
                                                       print(c,end="")
                                                  s = s[:-1]
                                                   
PYTHONPYTHOPYTHPYTPYP                         PYPYPYPYPYP
#注：break仅跳出当前最内层循环


4)循环的扩展
for <变量> in <遍历结构> :                   while <条件> :
    <语句块1>                                     <语句块1>
else :                                       else:      
    <语句块2>                                     <语句块2>

#注：当循环没有被break语句退出时，执行else语句块，else语句块作为"正常"完成循环的奖励，这里else的用法与异常处理中else用法相似

for c in "PYTHON":                                for c in "PYTHON" :
    if c == "T":                                     if c == "T" :
        continue                                        break   
    print(c,end="")                                  print(c,end="")
else:                                             else:
    print("正常退出")                                print("正常退出")

PYTHON正常退出                                    PY

'''


    
