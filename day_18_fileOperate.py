#文本形式打开文件
tf = open("f.txt","rt")
print(tf.readline())
tf.close()
>>>
#中国是个伟大的国家！

#二进制形式打开文件
bf = open("f.txt","rb")
print(bf.readline())
bf.close()

>>>
#b'\xd6\xd0\xb9\xfa\xca\xc7\xb8\xf6\xce\xb0
#\xb4\xf3\xb5\xc4\xb9\xfa\xbc\d2\xa3\a1'

#文件的打开关闭
#文件处理的步骤：打开-操作-关闭
'''
a = open(,)
<变量名> = open(<文件名>,         <打开模式>)
文件句柄        文件路径和名称    文本or二进制
                源文件同目录可省路径   读or写

打开模式
'r' 只读模式 默认值 如果文件不存在 返回FileNotFoundError
eg: f = open("f.txt")  /f = open("f.txt","rt")
'w' 覆盖模式 文件不存在则创建 存在则完全覆盖
eg: f = open("f.txt","w")
'x' 创建写模式 文件不存在则创建 存在则返回FileExitsError
eg: f = open("f.txt","x")
'a' 追加写模式 文件不存在则创建 存在则在文件最后追加内容
eg: f = open("f.txt","a+")
'b' 二进制文件模式
eg: f = open("f.txt","b") /f = open("f.txt","wb")
't' 文本文件模式 默认值
'+' 与r/w/x/a一同使用，在原功能基础上增加同时读写功能

文件由存储状态转为文件的占用状态

读文件
a.read(size)
读入全部内容，如果给出参数，读入前size长度
>>>s = f.read(2) #读入前2字节
a.readline(size)
读入一行内容，如果给出参数，读入该行前size长度
>>>s = f.readline()
a.readlines(hint)
读入文件所有行，以每行为元素行程列表
如果给出参数，读入前hint行
>>>s = f.readlines()

文件的全文本操作
遍历全文本：方法一
fname = input("请输入要打开的文件名称:")
fo = open(fname,"r")
txt = fo.read()   #一次读入，统一处理
#对全文txt进行处理
fo.close()

遍历全文本：方法二
fname = input("请输入要打开的文件名称：")
fo = open(fname,"r")
txt = fo.read(2)
while txt!= "":
#对txt进行处理     #按数量读入，逐步处理
    txt = fo.read(2)
fo.close()

文件的逐行操作
逐行遍历文件：方法一
fname = input("请输入要打开的文件名称：")
fo = open(fname,"r")
for line in fo.readlines():
    print(line)
fo.close()

逐行遍历文件：方法二
fname = input("请输入要打开的文件名称：")
fo = open(fname,"r")
for line in fo:
    print(line)    #分行读入，逐行处理
fo.close()


写文件
a.write(s)
向文件写入一个字符串或字节流
>>>f.write("中国是一个伟大的国家！")
a.writelines(lines)
将一个元素全为字符串的列表写入文件
>>>ls = ["中国","法国","美国"]
>>>f.writelines(ls)
中国法国美国
a.seek(offset)
改变当前文件操作指针的位置，offset含义如下：
0 - 文件开头； 1 - 当前位置；2 - 文件结尾
>>>f.seek(0) #回到文件开头

eg:
fo = open("output.txt","w+")
ls = ["中国","法国","美国"]
fo.writelines(ls)
for line in fo:   #写入一个字符串列表 >>>没有任何输出
    print(line)
fo.close()

数据的文件写入
fo = open("output.txt","w+")
ls = ["中国","法国","美国"]
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()



a.close()

'''
