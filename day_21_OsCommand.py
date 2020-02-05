#进程管理
'''
os.system(command)
执行程序或命令command
在windows系统中，返回值为cmd的调用返回信息

import os
os.system("C:\\Windows\\System32\\calc.exe")
>>>
0

import os
os.system("C:\\Windows\\System32\\mspaint.exe\
			D:\\PYECourse\\grwordcloud.png")
>>>
0

#环境参数
获取或改变系统环境信息
os.chdir(path) 修改当前程序操作的路径
>>>os.chdir("D:")

os.getcwd() 返回程序的当前路径
os.getcwd()
'D:\\'

os.getlogin() 获取当前系统登录用户名称
>>>os.getlogin()
'Tian Song'

os.cpu_count() 获取当前系统的CPU数量
>>>os.cpu_count()

os.urandom(n) 获得n个字节长度的随机字符串，通常用于加解密运算
>>>os.urandom(10)
b'7\xbe\xf2!\xc1=\x01gL\xb3'



'''
